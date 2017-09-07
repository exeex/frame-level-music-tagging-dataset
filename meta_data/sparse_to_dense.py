from read_csv_data import get_table, get_tags, write_csv ,transpose_table


def get_mp3_length_dict(table):

    d = dict()

    for row in table:
        d[str(row[0])]=int(row[1])

    return d

def time_to_frame_idx(time):

    if time == '':
        return None

    frames_per_second = 2
    frame_idx = frames_per_second*int(time)

    return frame_idx

table = get_table("100groundtruth.csv", delimiter=',')
ground_truth = transpose_table(table)
table2 = get_table("timelist.csv", delimiter=',')
dl = get_mp3_length_dict(table2)

print(dl)

# allocate space
d = {}
for song_id in list(set(ground_truth[0])):
    try:
        d[song_id]= dict()
        d[song_id]['male']=[0.0 for x in range(time_to_frame_idx(dl[song_id]))]
        d[song_id]['female']=[0.0 for x in range(time_to_frame_idx(dl[song_id]))]
    except KeyError:
        print("No data. song id :",song_id)

# build data

for row in table:
    song_id = row[0]
    female_in_t = row[1]
    female_out_t = row[2]
    male_in_t = row[3]
    male_out_t = row[4]

    male_in_f = time_to_frame_idx(male_in_t)
    male_out_f = time_to_frame_idx(male_out_t)
    female_in_f = time_to_frame_idx(female_in_t)
    female_out_f = time_to_frame_idx(female_out_t)

    # print(song_id,male_in_f,male_out_f,female_in_f,female_out_f)
    try:
        if male_in_f is not None:
            d[song_id]['male'][male_in_f:male_out_f] = [1.0 for x in range(male_out_f-male_in_f)]
        if female_in_f is not None:
            d[song_id]['female'][female_in_f:female_out_f] = [1.0 for x in range(female_out_f-female_in_f)]
    except KeyError:
        pass
# write csv
song_ids = list(set(ground_truth[0]))
song_ids.sort()

for song_id in song_ids:
    table_dense = []
    filename = "..\\tagged_data\\%03d.csv" % int(song_id)

    try:
        song = d[song_id]

        for idx in range(time_to_frame_idx(dl[song_id])):
            row = [int(song_id), song["male"][idx],song["female"][idx],filename]
            table_dense.append(row)

    except:
        continue
    write_csv(table_dense,filename=filename,tags=["frame_idx","male","female","filename"])








