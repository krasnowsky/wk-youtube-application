from dataclasses import dataclass
import string
from tokenize import String

@dataclass
class video:
    id: string
    url: string
    thumbnail: string
    published_at: string
    title: string