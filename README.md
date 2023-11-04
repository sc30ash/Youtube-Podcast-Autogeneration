# YouTube Video Creator from Latest News

This GitHub repository provides a Python script to create YouTube videos by scraping the latest news, summarizing articles, and storing the text in an Excel file. It also generates videos from images in the articles and uses text-to-speech to create an audio file using famous celebrity voices. The final video is uploaded to YouTube with SEO-optimized title.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Creating engaging YouTube videos from the latest news can be a time-consuming task. This repository streamlines the process by automating the following steps:
1. Scraping the latest news articles from various sources.
2. Summarizing the articles to create concise content.
3. Storing the summarized content in an Excel file.
4. Generating videos from the images within the articles.
5. Using text-to-speech technology to create an audio file with famous celebrity voices.
6. Uploading the video to YouTube with an SEO-optimized title.

## Requirements

Before using this repository, ensure that you have the following prerequisites:

- Python 3.x
- Python packages listed in the [requirements.txt](requirements.txt) file.
- YouTube API credentials (for video upload).

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Install the required Python packages.

```bash
pip install -r requirements.txt
```

3. Set up your YouTube API credentials by following [YouTube API Documentation](https://developers.google.com/youtube/registering_an_application).

## Usage

1. Configure the necessary settings in the `config.yml` file.
2. Run the `produce_video.py` script to execute the entire process.

```bash
python produce_video.py
```

The script will start scraping news, summarizing articles, creating video content, generating audio, and uploading the video to YouTube.

## Modules

This repository is organized into several modules:

- `scraper.py`: Contains functions for scraping news articles.
- `summarizer.py`: Handles article summarization.
- `excel_manager.py`: Manages Excel file creation and updating.
- `video_generator.py`: Creates video content from article images.
- `text_to_speech.py`: Generates audio using famous celebrity voices.
- `youtube_uploader.py`: Handles the YouTube video upload process.
- `produce_video.py`: The main script to execute the entire workflow.

You can explore and modify these modules to suit your needs.

## Configuration

The configuration settings for the entire process are stored in the `config.yml` file. Make sure to update this file with your specific preferences and API credentials.

## Contributing

If you want to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Test your changes thoroughly.
5. Create a pull request to this repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as you see fit.

For any questions or issues, please open a GitHub issue in this repository. Happy YouTube video creation! 📹🚀
