from dataclasses import dataclass
import time

@dataclass(unsafe_hash = True)
class Camping_review():
    camping_index : str
    review_idx : int
    user_id : str
    edited_time : time.strftime('%Y-%m-%d %H:%M:%S')
    review_content : str
