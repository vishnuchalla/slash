"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: vamsitadikonda99@gmail.com

"""
import datetime
import argparse
import scraper
import formatter
import email_utils
from tabulate import tabulate
from queue import Queue
from threading import Thread


def extractProducts(args):
    result_queue = Queue()
    search = args.search if isinstance(args,
                                       argparse.Namespace) else args['search']
    link = bool(args.link) if isinstance(args, argparse.Namespace) else bool(
        args.get('link', True))
    num = int(args.num) if isinstance(args, argparse.Namespace) else int(
        args.get('num', 3))
    sort = args.sort if isinstance(args, argparse.Namespace) else args.get(
        'sort', "re")
    des = bool(args.des) if isinstance(args, argparse.Namespace) else bool(
        args.get('des', True))

    t1 = Thread(
        target=scraper.searchAmazon,
        args=(
            search,
            link,
            result_queue,
            num,
        ),
    )
    t2 = Thread(
        target=scraper.searchWalmart,
        args=(
            search,
            link,
            result_queue,
            num,
        ),
    )
    t3 = Thread(
        target=scraper.searchTarget,
        args=(
            search,
            link,
            result_queue,
            num,
        ),
    )

    # Starting threads...
    t1.start()
    t2.start()
    t3.start()

    # Waiting for threads to finish execution...
    t1.join()
    t2.join()
    t3.join()

    result_list = [result_queue.get() for i in range(result_queue.qsize())]
    finalistList = [formatter.sortList(result_list, sort, des)[:num * 3]]

    mergedResults = email_utils.alternateMerge(finalistList)
    results = formatter.sortList(mergedResults, sort, des)
    return results


def send_email(results, args):
    email = args.email if isinstance(args, argparse.Namespace) else args.get(
        'email', "")
    link = bool(args.link) if isinstance(args, argparse.Namespace) else bool(
        args.get('link', True))
    try:
        if email:
            email_utils.write_data(results, link, email)
        return True
    except:
        return False


def main():
    """
    Argument parser to capture command line and trigger the workflow
    """
    start_time = datetime.datetime.now()
    parser = argparse.ArgumentParser(description="Slash")
    parser.add_argument('--search', type=str, help='Product search query')
    parser.add_argument('--num',
                        type=int,
                        help="Maximum number of records",
                        default=3)
    parser.add_argument(
        '--sort',
        type=str,
        nargs='+',
        help=
        "Sort according to re (relevance: default), pr (price) or ra (rating) or all",
        default="re")
    parser.add_argument('--link',
                        action='store_true',
                        help="Show links in the table")
    parser.add_argument('--des',
                        action='store_true',
                        help="Sort in descending (non-increasing) order")
    parser.add_argument('--email',
                        type=str,
                        default="",
                        help="list of email to get notified")
    args = parser.parse_args()

    results = extractProducts(args)

    print(tabulate(results, headers="keys", tablefmt="github"))
    send_email(results, args)
    end_time = datetime.datetime.now()
    print("t1:{},t1:{}, diff = {}".format(start_time, end_time,
                                          end_time - start_time))


if __name__ == '__main__':
    """
    Execution starts here.
    """
    main()
