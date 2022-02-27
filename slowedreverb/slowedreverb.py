def slowedreverb(audio, output):

    if '.wav' not in audio:
        print('Audio needs to be .wav!')
        return

    import soundfile as sf
    from pedalboard import Pedalboard, Reverb
    from math import trunc

    # Import audio file
    print('Importing audio...')
    audio, sample_rate = sf.read(audio)

    # Slow audio
    print('Slowing audio...')
    sample_rate -= trunc(sample_rate*0.08)

    # Add reverb
    print('Adding reverb...')
    board = Pedalboard([Reverb(
        room_size=0.75,
        damping=0.5,
        wet_level=0.08,
        dry_level=0.2
        )])

    # Add effects
    effected = board(audio, sample_rate)

    # Export audio
    print('Exporting audio...')
    sf.write(output, effected, sample_rate)