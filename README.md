# Overview

## What

A short script that will poll a specified YouTube channel when run and generate a iTunes compatible podcast feed for use on various iDevices.

## Why

I do a lot of walking and I like to be able download a ton of content to my iPhone before leaving to listen to while I'm out.

Originally wrote this to give me a podcast feed of the Mindcrack Network (http://www.youtube.com/user/MindCrackNetwork).

It is designed to run as a nightly cron job on a space and processor resource limited Raspberry Pi. To offset these limits I used Amazon S3 for storage and Amazon Elastic Transcoder to get it in the format that the iPhone podcasts app expects. However, I tried to make everything as modular as possible, so anyone should be able to repurpose this to use local resources pretty easily.

## How

When run, the script will do the following:

1. Visit the YouTube channel specified
2. Check for new videos (goes back 10 by default, but this can be changed)
3. Download an audio-only version of the file (mp4)
4. Upload the file to Amazon S3
5. Transcode the file into an MP3 using Amazon Elastic Transcoder (the iPhone doesn't like the m4a format off direct off of YouTube)
6. Spit out a podcast-able (at with iTunes) RSS file and uploads it to Amazon S3

By default, media files are named with their video id (x3svDHLKulU.mp3) and outputted RSS feeds are named by their channel name (mindcracknetwork.xml). This allows you to use this script multiple times if you want more than one channel in podcast format.

# Getting Started

## Setting up your environment

I used virtualenv for all of this. All you need to do is spin up a virtual environment, and then run:

> pip install -r requirements.txt 

You will also need to fill out the config\_template.py file, rename it config.py and create a .boto configuration file.

The .boto configuration file is documented at: http://docs.pythonboto.org/en/latest/boto_config_tut.html
