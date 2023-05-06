#! /usr/bin/env bash
set -e

watchfiles --filter python  'celery -A src.worker.celery worker --loglevel=info'
