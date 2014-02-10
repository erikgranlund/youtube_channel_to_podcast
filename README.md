## What

A short script that will poll a specified YouTube channel when run and generate a iTunes compatible podcast feed for use on various iDevices

## Why

I do a lot of walking and I like to be able download a ton of content to my iPhone before leaving to listen to while I'm out.

Originally wrote this to give me a podcast feed of the Mindcrack Network (http://www.youtube.com/user/MindCrackNetwork).

## How

When run, the script will do the following:

1. Visit the YouTube channel specified
2. Check for new videos (goes back to the past 10)
3. Download an MP3 version of the video (uses the vid2mp3 module)
4. (optional) Upload the MP3 file to Amazon S3 (this was written to be run on a Raspberry Pi where space is at a premium)
5. Spits out a podcast-able (at with iTunes) RSS file which can be copied to a website accessible from whatever iDevice you want.

## Other

This should go saying, but I'm going to say it anyway. You probably shouldn't use this script to download and publicly host content that is not yours without the content owners permission.
