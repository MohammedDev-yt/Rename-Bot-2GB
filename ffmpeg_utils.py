
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_file, output_file, title, author, artist, audio, subtitle, video):

    try:  
        # -------- STEP 1: FAST COPY -------- #  
        stream = ffmpeg.input(input_file)  

        stream = ffmpeg.output(  
            stream,  
            output_file,  

            vcodec="copy",  
            acodec="copy",  
            map="0",  
            map_metadata="-1",  

            **{  
                "metadata": f"title={title}",  
                "metadata:g": f"artist={artist}",  
                "metadata:g:1": f"author={author}",  
                "metadata:s:a:0": f"title={audio}",  
                "metadata:s:s:0": f"title={subtitle}",  
                "metadata:s:v:0": f"title={video}",  
            },  

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
        print("⚠️ Cᴏᴘʏ Fᴀɪʟᴇᴅ, Sᴡɪᴛᴄʜɪɴɢ Tᴏ Rᴇ-Eɴᴄᴏᴅᴇ:", e)  

        # -------- STEP 3: FALLBACK RE-ENCODE -------- #  
        try:  
            stream = ffmpeg.input(input_file)  

            stream = ffmpeg.output(  
                stream,  
                output_file,  

                vcodec="copy",  
                acodec="copy",  
                map="0",  

                movflags="+faststart",  
              
                **{  
                    "metadata": f"title={title}",  
                    "metadata:g": f"artist={artist}",  
                    "metadata:g:1": f"author={author}",  
                  }  
            )  

            ffmpeg.run(stream, overwrite_output=True)  
            return output_file  

        except Exception as e2:  
            print("❌ Rᴇ-Eɴᴄᴏᴅᴇ Aʟsᴏ Fᴀɪʟᴇᴅ:", e2)  
            return input_file

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #