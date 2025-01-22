#!/bin/bash
source antenv/bin/activate
gunicorn -w 4 -b 0.0.0.0:$PORT fakedata:app
