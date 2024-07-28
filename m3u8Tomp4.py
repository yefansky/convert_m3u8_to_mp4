import subprocess
import argparse
import os

def sanitize_filename(name: str) -> str:
    # 截断文件名中的空格和点号
    for char in [' ', '.']:
        if char in name:
            name = name.split(char)[0]
    return name

def convert_m3u8_to_mp4(input_dir: str):
    # 查找输入目录中的 index.m3u8 文件
    m3u8_file = os.path.join(input_dir, 'index.m3u8')
    if not os.path.isfile(m3u8_file):
        print(f"找不到文件: {m3u8_file}")
        return

    # 获取目录的最后一级名称并生成输出文件名
    dir_name = os.path.basename(os.path.normpath(input_dir))
    output_name = sanitize_filename(dir_name) + '.mp4'
    output_file = os.path.join(input_dir, output_name)

    # 调用FFmpeg命令，将M3U8文件转换为MP4
    command = [
        'ffmpeg',
        '-i', m3u8_file,
        '-c', 'copy',  # 直接拷贝流，不重新编码
        '-bsf:a', 'aac_adtstoasc',  # 转换音频格式
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"转换成功：{output_file}")
    except subprocess.CalledProcessError as e:
        print(f"转换失败：{e}")

def main():
    # 设置命令行参数解析器
    parser = argparse.ArgumentParser(description='Convert M3U8 in a directory to MP4.')
    parser.add_argument('input_dir', help='Path to the directory containing the index.m3u8 file.')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用转换函数
    convert_m3u8_to_mp4(args.input_dir)

if __name__ == "__main__":
    main()
