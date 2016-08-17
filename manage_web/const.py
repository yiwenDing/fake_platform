# -*- coding: utf-8 -*-

import re


ITEM_GROUP_PATTERN = re.compile(r'^g(?P<id>[0-9]+)$')
ITEM_CONTENT_GROUP_PATTERN = re.compile(r'^cg(?P<id>[0-9]+)$')
ITEM_AD_PATTERN = re.compile(r'^a(?P<id>[0-9]+)\.(?P<mode>[0-4])$')
ITEM_CHANNEL_EXPLORE_BLOCK_PATTERN = re.compile(r'^channel_explore_block$')
ITEM_SUBJECT_CARD_PATTERN = re.compile(r'^subject_card:(?P<id>[0-9]+)$')
ITEM_CHANNEL_EXPLORE_PATTERN = re.compile(r'^channel_explore:(?P<category>[a-zA-Z_]+)$')
ITEM_CHANNEL_EXPLORE_CARD_PATTERN = re.compile(r'^channel_explore_card\((?P<categories>[a-zA-Z_]+(,[a-zA-Z_]+)*)\)$')