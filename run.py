import argparse
import time

from data import JsonWriter
from crawl import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--crawl', type=str, required=True)
    parser.add_argument('--start', type=str, required=True)
    parser.add_argument('--end', type=str, required=True)
    parser.add_argument('--uid', type=int, default=-1)
    parser.add_argument('--max-page', type=int, default=10)
    parser.add_argument('--num-per-page', type=int, default=20)
    parser.add_argument('--output-path', type=str, default=None)
    parser.add_argument('--audience-list', type=str, default='')

    args = parser.parse_args()
    output_path = args.output_path
    if args.crawl == 'l':
        if output_path is None:
            output_path = 'list_{}_{}_{}-per-month'.format(
                args.start, args.end, str(args.num_per_page * args.max_page))
        with JsonWriter(output_path) as writer:
            items = get_audience_list_by_month(start_month=args.start, end_month=args.end, max_page=args.max_page)
            for item in items:
                writer.write(item)
    elif args.crawl == 'ad':
        assert args.uid != -1
        if output_path is None:
            output_path = 'detail_{}_{}_{}'.format(args.uid, args.start, args.end)
        with JsonWriter(output_path) as writer:
            items = get_audience_detail_by_day(args.uid, args.start, args.end)
            for item in items:
                writer.write(item)
    elif args.crawl == 'md' or args.crawl == 'mm':
        assert args.audience_list != ''
        with open(args.audience_list, 'r', encoding='utf-8') as f:
            audience_list = [uid.strip() for uid in f.readlines()]
        if output_path is None:
            output_path = 'detail_{}_audiences_{}_{}'.format(len(audience_list), args.start, args.end)
        with JsonWriter(output_path) as writer:
            for uid in audience_list:
                if args.crawl == 'md':
                    items = get_audience_detail_by_day(uid, args.start, args.end)
                elif args.crawl == 'mm':
                    items = get_audience_detail_by_month(uid, args.start, args.end)
                for item in items:
                    writer.write(item)
                time.sleep(10)
    else:
        raise argparse.ArgumentError
