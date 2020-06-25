#!/bin/bash

curl https://www.wired.com/2012/09/star-trek-one-liners/ |html2text |grep -e "^[0-9]" > responses

