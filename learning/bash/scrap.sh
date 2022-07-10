#!/bin/bash
└──╼ $curl https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops | sed -e 's/<[^>]+>//'

$grep "price" laptops.txt | cut -d ">" -f2 | cut -d "<" -f1