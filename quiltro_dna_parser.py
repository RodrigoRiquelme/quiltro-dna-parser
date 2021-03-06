from PIL import Image


class QuiltroDnaParser:

    def __init__(self, image=None):
        self.rotation = 90
        self.colour_map = {
            0: (255, 255, 255),  # White
            1: (255, 255, 0),  # Yellow
            2: (0, 0, 0),  # Black
            3: (128, 255, 0),  # Lime
            4: (0, 64, 255),  # Crayon Blue
            5: (192, 0, 255),  # Purple
            6: (255, 128, 0),  # Orange
            7: (0, 255, 255),  # Aqua
            8: (255, 0, 255)  # Fuchsia
        }

        if image:
            self.im = Image.open(image).rotate(self.rotation)
            self.pixels = list(self.im.getdata())
            self.width, self.height = self.im.size

    def preview(self):
        pixel_string = ''
        for i in range(self.height):
            pixel_line = ''
            for pixel in self.pixels[i * self.width:(i + 1) * self.width]:
                pixel_line = pixel_line + str(pixel)
            pixel_string = pixel_string + pixel_line + '\n'
        return pixel_string

    def output_ppm(self):
        ppm_string = ''
        for i in range(self.height):
            pixel_line = ''
            for pixel in self.pixels[i * self.width:(i + 1) * self.width]:
                pixel_line = pixel_line + str(pixel)
            ppm_string = ppm_string + pixel_line + '.'
        return ppm_string[:-1]

    def write_ppm(self, filename):
        ppm = self.output_ppm()
        f = open(filename, "w")
        f.write(ppm)
        f.close()

    def image_from_ppm(self, ppm, filename):
        width = 0
        height = 0
        img_data = []
        for i in ppm.split('.'):
            width = len(i)
            height = height + 1
            for s in i:
                img_data.append(int(s))
        z = 0
        print height, width
        img = Image.new('RGB', (height, width))
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = self.colour_map[img_data[z]]
                img.putpixel((x, y), (r, g, b))
                z = z + 1
        img.save(filename, save_all=True, append_images=[img])

    def image_from_ppm_file(self, input_file, output_filename):
        ppm = self.file_get_contents(input_file)
        ppm = ppm.replace('\n', '.')
        return self.image_from_ppm(ppm, output_filename)

    @staticmethod
    def file_get_contents(filename):
        with open(filename) as f:
            return f.read()
