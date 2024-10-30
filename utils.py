from PIL import Image, ImageOps


def compress_image():
    # 打开GIF图像
    input_path = 'img/r2gs.png'
    output_path = 'img/r2gs_covert.png'
    image = Image.open(input_path)

    # 反转图像颜色
    inverted_image = ImageOps.invert(image.convert("RGB"))

    # 保存置反后的图像
    inverted_image.save(output_path)
    # image.save(output_path, save_all=True, loop=0, duration=5)


if __name__ == '__main__':
    compress_image()
