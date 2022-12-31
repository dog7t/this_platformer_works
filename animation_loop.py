current_frame = 1
total_frames = 6
adding_frames = 0
while True:    
    current_frame = (current_frame + 1) % total_frames
    print(current_frame)
    adding_frames += 1
    if adding_frames == 50:
        break