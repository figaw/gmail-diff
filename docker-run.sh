#!/bin/sh

docker run --rm \
    -e GMAIL_FIRST_USER \
    -e GMAIL_FIRST_PASSWORD \
    -e GMAIL_SECOND_USER \
    -e GMAIL_SECOND_PASSWORD \
    figaw/gmail-diff:1.0.0 > output.txt
