# Color Palette Generator

The Color Palette Generator is a web application designed for effortlessly creating color palettes from your uploaded images. Whether you're a designer seeking inspiration or simply curious about the colors within an image, this tool can help you extract and visualize the color palette.

## Key Features

- **Image Upload**: Easily upload images in popular formats like JPEG, JPG, and PNG.

- **Color Palette Generation**: The application analyzes the uploaded image and extracts dominant colors, generating a cohesive color palette.

- **Real-time Preview**: Instantly view the generated color palette with corresponding color codes.

- **Generate a New Palette**: If the current palette doesn't meet your needs, simply click the "Try another" button to generate a fresh one.

- **Responsive Design**: The application is optimized for seamless use on both desktop and mobile devices.

- **Vibrant UI**: Enjoy an engaging and visually appealing user interface with a rainbow-themed design.

## Getting Started

To set up and run the Color Palette Generator on your local machine, follow the steps below:

### Prerequisites

Ensure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/) (Version 3.7 or higher)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (For managing Python virtual environments)

### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/color-palette-generator.git
cd color-palette-generator
```

2. Create a Virtual Environment:

If you don't have virtualenv installed, you can install it using pip:

```bash
pip install virtualenv
```
Then, create and activate a virtual environment:

```bash
virtualenv venv
source venv/bin/activate
```

3. Install Dependencies:

Use pip to install the required Python packages:
```bash
pip install -r requirements.txt
```

### Usage

1. Run the Application:

Start the Flask application by running the following command:

```bash
flask run
```

The application will start, and you'll see output indicating that it's running on a local server.

2. Access the Application:

Open your web browser and navigate to http://localhost:5000 to access the Color Palette Generator.

3. Upload an Image:

Upload an image either by dragging and dropping it onto the designated area or by clicking to select a file from your computer.

4. Generate a Color Palette:

After uploading an image, click the "Generate" button. The application will analyze the image and display the color palette extracted from it.

5. Explore the Palette:

Explore the colors in the palette, along with their corresponding color codes.

6. Generate a New Palette:

If you're not satisfied with the current palette, you can generate a new one by clicking the "Try another" button.

This concludes the installation and usage guide for the Color Palette Generator. Enjoy exploring color palettes from your images!

## License

This project is licensed under the MIT License.
