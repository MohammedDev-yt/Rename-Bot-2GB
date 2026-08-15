# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_file, output_file, title, author, artist, video):

    try:
        # -------- STEP 1: FAST COPY -------- #
        stream = ffmpeg.input(input_file)

        stream = ffmpeg.output(
            stream,
            output_file,

            # Keep ALL streams exactly as they are
            vcodec="copy",
            acodec="copy",
            map="0",

            # Remove old container metadata
            map_metadata="-1",

            # Add only requested metadata
            **{
                "metadata": f"title={title}",
                "metadata:g:artist": f"{artist}",
                "metadata:g:author": f"{author}",
                "metadata:s:v:0": f"title={video}",
            },

            # Don't re-encode streams
            movflags="+faststart",
        )

        ffmpeg.run(stream, overwrite_output=True)

        # -------- STEP 2: VALIDATE OUTPUT -------- #
        if not os.path.exists(output_file):
            raise Exception("Output not created")

        size = os.path.getsize(output_file)

        if size < 100000:
            raise Exception("Broken file")

        return output_file

    except Exception as e:
        print("⚠️ Cᴏᴘʏ Fᴀɪʟᴇᴅ:", e)

        # -------- STEP 3: SAFE FALLBACK -------- #
        try:
            stream = ffmpeg.input(input_file)

            stream = ffmpeg.output(
                stream,
                output_file,

                # Keep every stream unchanged
                vcodec="copy",
                acodec="copy",
                map="0",

                # Only general metadata
                **{
                    "metadata": f"title={title}",
                    "metadata:g:artist": f"{artist}",
                    "metadata:g:author": f"{author}",
                }
            )

            ffmpeg.run(stream, overwrite_output=True)

            if os.path.exists(output_file):
                return output_file

        except Exception as e2:
            print("❌ Fᴀʟʟʙᴀᴄᴋ Fᴀɪʟᴇᴅ:", e2)

        return input_file


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #