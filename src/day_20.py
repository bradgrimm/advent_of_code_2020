import os

import numpy as np
from scipy.signal import convolve2d

from utils import load_day

photo_data = load_day(20, sample=False, split=False).split('\n\n')
w = int(np.sqrt(len(photo_data)))


def parse_all_photos(photo_data):
    photos = {}
    for photo in photo_data:
        photo_raw = photo.split('\n')
        photo_id = photo_raw[0].replace(':', '').split()[1]
        photo = np.array([
            [c == '#' for c in p]
            for p in photo_raw[1:]
        ])
        photos[photo_id] = photo
    return photos


def all_orientations(photo):
    photos = []
    for flip in [False, True]:
        p = photo.copy()
        if flip:
            p = np.fliplr(p)
        for _ in range(4):
            photos.append(p)
            p = np.rot90(p)
    return photos


def initial_layouts(photos):
    possible_layouts = []
    for p_id, photo in photos.items():
        rot_photos = all_orientations(photo)
        possible_layouts.extend([
            ([p_id], [p], set(photos.keys()) - {p_id})
            for p in rot_photos
        ])
    return possible_layouts


def can_stitch_right(p1, p2):
    return np.all(p1[:, -1] == p2[:, 0])


def can_stitch_down(p1, p2):
    return np.all(p1[-1, :] == p2[0, :])


def stitch_fits(stitched, photo):
    n = len(stitched)
    top, left = True, True
    if n >= w:
        top = can_stitch_down(stitched[n-w], photo)
    if n % w != 0:
        left = can_stitch_right(stitched[n-1], photo)
    return top and left


def find_stitched_photo(photos):
    possible_layouts = initial_layouts(photos)
    while possible_layouts:
        stitched_ids, stitched, options = possible_layouts.pop()
        if len(stitched) == len(photos):
            break
        for p_id in options:
            option = photos[p_id]
            for p2 in all_orientations(option):
                if stitch_fits(stitched, p2):
                    new_ids = list(stitched_ids) + [p_id]
                    new_stitched = list(stitched) + [p2]
                    new_options = set(options) - {p_id}
                    possible_layouts.append((new_ids, new_stitched, new_options))
    return stitched_ids, stitched


def find_and_remove_sea_monsters(img, monster):
    cleared_img = img.copy().astype(int)
    m_cnt = monster.sum()
    for rot_mon in all_orientations(monster):
        t = convolve2d(img.astype(float), rot_mon.astype(float), mode='same')
        if len(t[t == m_cnt]) > 0:
            m_sz = rot_mon.shape
            center_offset = (m_sz[0] // 2, m_sz[1] // 2)
            sm_offset = np.argwhere(t == m_cnt) - center_offset
            lg_offset = sm_offset + m_sz
            for sm, lg in zip(sm_offset, lg_offset):
                cleared_img[sm[0]:lg[0], sm[1]:lg[1]] -= rot_mon
            break
    return cleared_img


photos = parse_all_photos(photo_data)

# Part 1
stitched_ids, stitched = find_stitched_photo(photos)
corners = [
    stitched_ids[0],
    stitched_ids[w-1],
    stitched_ids[(w-1) * w],
    stitched_ids[-1],
]
c_prod = np.array(corners).astype(int).prod()
print(f'Part 1: {c_prod}')


# Part 2
monster_str = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')
monster = np.array([
    [c == '#' for c in p]
    for p in monster_str
])
img_blocks = [s[1:-1, 1:-1] for s in stitched]
img = np.block([img_blocks[i*w:i*w+w] for i in range(w)])
waters = find_and_remove_sea_monsters(img, monster)
print(f'Part 2: {waters.sum()}')

