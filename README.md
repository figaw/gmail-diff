# Gmail Diff Tool

A basic tool that will diff two Gmail accounts.
For when you're doing a manual migration with e.g. Thunderbird,
and you want to see how far along you are in the process.

It prints all the folders,
the number of emails in each folder
and you can diff this to see how your migration has come along.

## Prerequisites

- Docker*

> You can run without Docker if you have Python3,
> and just install the `requirements.txt`.

### Environment Variables

```shell
export GMAIL_FIRST_USER="user1@doma1n.com"
export GMAIL_FIRST_PASSWORD="password1"
export GMAIL_SECOND_USER="user2@doma2n.net"
export GMAIL_SECOND_PASSWORD="password2"
```

> If you're using 2FA you "might" benefit from using
> an App Password:
> [Sign in using App Passwords](https://support.google.com/mail/answer/185833?hl=en).

## Usage (Python3)

1. Source the environment variables above.
1. `pip3 install --no-cache-dir -r requirements.txt`
1. `python3 ./list.py > output.txt`

## Usage (Docker)

1. Source the environment variables above.
1. Build the image with `./docker-build.sh`
1. Run the image with `./docker-run.sh`

## Using the output

- The file `output.txt` will now contain
  - a list of the folders in either email,
  - the number of emails in each folder,
  - separated by `---`
- Split `output.txt` into two files and diff them,
to see the difference between the two accounts.
