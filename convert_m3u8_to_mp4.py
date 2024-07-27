import subprocess
import argparse

def convert_m3u8_to_mp4(m3u8_file: str, output_file: str):
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
    parser = argparse.ArgumentParser(description='Convert M3U8 to MP4.')
    parser.add_argument('m3u8_path', help='Path to the M3U8 file.')
    parser.add_argument('output_mp4', help='Output path for the MP4 file.')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用转换函数
    convert_m3u8_to_mp4(args.m3u8_path, args.output_mp4)

if __name__ == "__main__":
    main()
