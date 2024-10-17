"""
The Proxy pattern is a structural design pattern that allows for the creation of a surrogate object
that acts as a placeholder for another object. This surrogate object, or proxy, can be used to control access
to the original object, or to add additional functionality to it.

The Proxy pattern is useful in situations where it may be expensive or impractical to create the original object,
or where there are access restrictions to the original object that need to be enforced.
By using a proxy object, clients can interact with the original object as if it were the real object,
but the proxy can perform additional tasks such as caching, validation, or security checks.
"""


class Image:
    def __init__(self, filename):
        self.filename = filename

    def display(self):
        print(f"Displaying image {self.filename}")


class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def display(self):
        if self.image is None:
            self.image = Image(self.filename)
        self.image.display()


if __name__ == "__main__":
    image1 = ImageProxy("image1.png")
    image2 = ImageProxy("image2.png")

    image1.display()  # Image loaded from disk and displayed
    image1.display()  # Image loaded from cache and displayed
    image2.display()  # Image loaded from disk and displayed
    image2.display()  # Image loaded from cache and displayed
