
# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #

import os
import re
import asyncio
import json
from google import genai
from google.genai import types
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from pyrogram import Client, filters, StopPropagation
from pyrogram.enums import ParseMode
from urllib.parse import quote
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from config import WEATHER_API, GEMINI_API_KEY, OWNER_ID 

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

MAINTENANCE = {
    "enabled": False,
    "reason": "Bot Is Uploading and Fixing Errors and Bugs"
}

# ==============================
# ADMIN VARIABLES
# ==============================

BOT_START = datetime.now()

CACHE = {}

FEEDBACK_IMAGE = "https://graph.org/file/ac5e24a6243bfbbbecca2-7210d817a7005a0f56.jpg"
DB_IMAGE = "https://graph.org/file/faf795187aa693e1024a4-746b376c8dcc889d4f.jpg"
CACHE_IMAGE = "https://graph.org/file/a49a09e10235fc020e604-289b1b02951a23f44b.jpg"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import os
import qrcode
import requests
import pytz
import imageio
import psutil
import shutil

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

WEATHER_CACHE = {}
QR_CACHE = {}
LAST_CACHE_CLEAR = "Never"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def register_tools(bot):

    # ---------------- QR CODE ---------------- #
    @bot.on_message(filters.command("qrcode"))
    async def qrcode_cmd(_, message):
        if len(message.command) < 2:
            return await message.reply_text(
                "Usage:\n/qrcode ʏᴏᴜʀ ᴛᴇxᴛ ᴏʀ ʟɪɴᴋ"
            )
        text = message.text.split(None, 1)[1]
        QR_CACHE[message.from_user.id] = text
        wait = await message.reply_text(
            "📱 <b>Gᴇɴᴇʀᴀᴛɪɴɢ Qʀ Cᴏᴅᴇ...</b>\n"
            "⏳ Pʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ...",
            parse_mode=ParseMode.HTML
        )
        try:
            qr = qrcode.QRCode(
               version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size=10,
               border=4
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            img = qr.make_image(
                fill_color="black",
                back_color="white"
            )
            file = f"qrcode_{message.from_user.id}.png"
            img.save(file)
            
            await wait.delete()
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ɴᴇᴡ ǫʀ ᴄᴏᴅᴇ •",
                            callback_data="new_qr"
                        ),
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
            await message.reply_photo(
                photo=file,
                caption=(
                    "📱 <b>Qʀ Cᴏᴅᴇ Gᴇɴᴇʀᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ</b>\n"
                    " ʙʏ @Aero_Unity\n\n"
                    f"<code>{text}</code>"
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=buttons
            )

            os.remove(file)

        except Exception as e:

            await wait.edit_text(
                f"❌ Error:\n{e}"
            )

    # ---------------- NEW QR ---------------- #
    @bot.on_callback_query(filters.regex("^new_qr$"))
    async def new_qr(_, query):

        user_id = query.from_user.id

        text = QR_CACHE.get(user_id)
        
        if not text:
            return await query.answer(
                "Nᴏ ᴘʀᴇᴄɪᴏᴜs ǫʀ ᴄᴏᴅᴇ ғᴏᴜɴᴅ.",
                show_alert=True
            )
        await query.answer()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )
        file = f"qrcode_{user_id}.png"
        img.save(file)
        
        await query.message.reply_photo(
            photo=file,
            caption=(
                "📱 <b>Qʀ Cᴏᴅᴇ Gᴇɴᴇʀᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ</b>\n"
                " ʙʏ @Aero_Unity\n\n"
                f"<code>{text}</code>"
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ɴᴇᴡ ǫʀ ᴄᴏᴅᴇ •",
                            callback_data="new_qr"
                        ),
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )
        os.remove(file)

    # ---------------- DATETIME ---------------- #
    @bot.on_message(filters.command("datetime"))
    async def datetime_cmd(_, message):

        wait = await message.reply_text(
            "🕒 <b>Gᴇᴛᴛɪɴɢ Cᴜʀʀᴇɴᴛ Dᴀᴛᴇ & Tɪᴍᴇ...</b>\n"
            "⏳ Pʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ..",
            parse_mode=ParseMode.HTML
        )
        try:
            zones = {
                "🇬🇧 UTC": "UTC",
                "🇮🇳 IST": "Asia/Kolkata",
                "🇦🇪 GST": "Asia/Dubai",
                "🇸🇬 SGT": "Asia/Singapore",
                "🇯🇵 JST": "Asia/Tokyo",
                "🇺🇸 EST": "America/New_York",
                "🇺🇸 PST": "America/Los_Angeles",
                "🇪🇺 CET": "Europe/Paris",
                "🇷🇺 MSK": "Europe/Moscow",
                "🇦🇺 AEST": "Australia/Sydney"
            }
            text = "🕐 <b>Cᴜʀʀᴇɴᴛ Dᴀᴛᴇ & Tɪᴍᴇ</b>\n\n"
            for name, zone in zones.items():

                tz = pytz.timezone(zone)
                now = datetime.now(tz)

                offset = now.strftime("%z")

                if offset:
                    hrs = int(offset[:3])
                    mins = int(offset[3:]) // 60

                    if mins == 0:
                        utc = f"UTC{hrs:+d}"
                    else:
                        utc = f"UTC{hrs:+d}.{mins}"
                else:
                    utc = "UTC"

                text += (
                    f"» {name}: "
                    f"<code>{now.strftime('%d/%m/%Y %H:%M')}</code> "
                    f"{utc}\n"
                )

            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ʀᴇғʀᴇsʜ •",
                            callback_data="refresh_datetime"
                        ),
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )

            await wait.delete()

            await message.reply_text(
                text,
                parse_mode=ParseMode.HTML,
                reply_markup=buttons
            )
        except Exception as e:

            await wait.edit_text(
                f"❌ Error:\n{e}"
            )

    # ---------------- REFRESH DATETIME ---------------- #
    @bot.on_callback_query(filters.regex("^refresh_datetime$"))
    async def refresh_datetime(_, query):

        await query.answer()
        zones = {
            "🇬🇧 UTC": "UTC",
            "🇮🇳 IST": "Asia/Kolkata",
            "🇦🇪 GST": "Asia/Dubai",
            "🇸🇬 SGT": "Asia/Singapore",
            "🇯🇵 JST": "Asia/Tokyo",
            "🇺🇸 EST": "America/New_York",
            "🇺🇸 PST": "America/Los_Angeles",
            "🇪🇺 CET": "Europe/Paris",
            "🇷🇺 MSK": "Europe/Moscow",
            "🇦🇺 AEST": "Australia/Sydney"
        }
        text = "🕐 <b>Cᴜʀʀᴇɴᴛ Dᴀᴛᴇ & Tɪᴍᴇ</b>\n\n"

        for name, zone in zones.items():

            tz = pytz.timezone(zone)
            now = datetime.now(tz)

            offset = now.strftime("%z")

            if offset:
                hrs = int(offset[:3])
                mins = int(offset[3:]) // 60

                if mins == 0:
                    utc = f"UTC{hrs:+d}"
                else:
                    utc = f"UTC{hrs:+d}.{mins}"
            else:
                utc = "UTC"

            text += (
                f"» {name}: "
                f"<code>{now.strftime('%d/%m/%Y %H:%M')}</code> "
                f"{utc}\n"
            )

        try:
            await query.message.edit_text(
                text,
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• ʀᴇғʀᴇsʜ •",
                                callback_data="refresh_datetime"
                            ),
                            InlineKeyboardButton(
                                "• ᴄʟᴏsᴇ •",
                                callback_data="close"
                            )
                        ]
                    ]
                )
            )
        except Exception:
            pass
        
    # ---------------- TEXT TO GIF ---------------- #
    @bot.on_message(filters.command("text2gif"))
    async def text2gif(_, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "Usage:\n/text2gif ʏᴏᴜʀ ᴛᴇxᴛ"
            )
        text = message.text.split(None, 1)[1]
        wait = await message.reply_text(
            "🎞 <b>Gᴇɴᴇʀᴀᴛɪɴɢ Gɪғ...</b>\n"
            "⏳ Pʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ...",
            parse_mode=ParseMode.HTML
        )
        try:
            frames = []

            for i in range(15):

                img = Image.new(
                    "RGB",
                    (800, 300),
                    (25, 25, 25)
                )

                draw = ImageDraw.Draw(img)

                try:
                    font = ImageFont.truetype(
                        "arial.ttf",
                        45
                    )
                except:
                    font = ImageFont.load_default()

                x = 30 + (i * 15)

                draw.text(
                    (x, 120),
                    text,
                    fill=(255, 255, 255),
                    font=font
                )

                frames.append(img)

            gif_file = f"textgif_{message.from_user.id}.gif"

            imageio.mimsave(
                gif_file,
                frames,
                duration=0.10
            )
            await wait.delete()

            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴜᴘᴅᴀᴛᴇs •",
                            url="https://t.me/Aero_Unity"
                        ),
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
            await message.reply_animation(
                animation=gif_file,
                caption=(
                    "🎞 <b>Tᴇxᴛ Tᴏ Gɪғ</b>\n\n"
                    f"<code>{text}</code>"
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=buttons
            )
            os.remove(gif_file)

        except Exception as e:

            await wait.edit_text(
                f"❌ Error:\n{e}"
            )

    # ---------------- WEATHER ---------------- #
    @bot.on_message(filters.command("weather"))
    async def weather_cmd(_, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "Usage:\n/weather ᴄɪᴛʏ ɴᴀᴍᴇ"
            )
        city = message.text.split(None, 1)[1].strip()
        WEATHER_CACHE[message.from_user.id] = city
        wait = await message.reply_text(
            "🌦 <b>Fᴇᴛᴄʜɪɴɢ Wᴇᴀᴛʜᴇʀ...</b>\n"
            "⏳ Pʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ...",
            parse_mode=ParseMode.HTML
        )
        try:
            # -------- GEO SEARCH -------- #

            geo_url = (
                f"http://api.openweathermap.org/geo/1.0/direct"
                f"?q={quote(city)}"
                f"&limit=1"
                f"&appid={WEATHER_API}"
            )

            geo = requests.get(
                geo_url,
                timeout=20
            ).json()

            if not geo:
                return await wait.edit_text(
                    "‼️ ᴄʜᴇᴄᴋ ᴛʜᴇ sᴘᴇʟʟɪɴɢ ᴛʀʏ ᴀɢᴀɪɴ ᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ᴄɪᴛʏ ɴᴏᴛ ғᴏᴜɴᴅ"
                )

            place = geo[0]

            lat = place["lat"]
            lon = place["lon"]

            city_name = place["name"]
            state = place.get("state", "")
            country = place["country"]   
      
            # -------- CURRENT WEATHER -------- #
            current_url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?lat={lat}"
                f"&lon={lon}"
                f"&appid={WEATHER_API}"
                f"&units=metric"
            )
            current = requests.get(
                current_url,
                timeout=20
            ).json()
        
            # -------- FORECAST -------- #
            forecast_url = (
                f"https://api.openweathermap.org/data/2.5/forecast"
                f"?lat={lat}"
                f"&lon={lon}"
                f"&appid={WEATHER_API}"
                f"&units=metric"
            )

            forecast = requests.get(
                forecast_url,
                timeout=20
            ).json()

            temp = round(current["main"]["temp"])
            feels = round(current["main"]["feels_like"])

            temp_f = round((temp * 9 / 5) + 32)
            feels_f = round((feels * 9 / 5) + 32)

            condition = current["weather"][0]["main"]

            humidity = current["main"]["humidity"]

            wind = round(current["wind"]["speed"] * 3.6)

            visibility = round(current["visibility"] / 1000)

            pressure = current["main"]["pressure"]

            clouds = current["clouds"]["all"]

            uv = "0"
            uv_text = "Low"

            days = {}

            for item in forecast["list"]:

                day = item["dt_txt"].split()[0]

                if day not in days:

                    days[day] = {
                        "min": item["main"]["temp_min"],
                        "max": item["main"]["temp_max"],
                        "weather": item["weather"][0]["main"]
                    }

                else:

                    days[day]["min"] = min(
                        days[day]["min"],
                        item["main"]["temp_min"]
                    )

                    days[day]["max"] = max(
                        days[day]["max"],
                        item["main"]["temp_max"]
                    )

            forecast_text = ""

            count = 0

            for day, value in days.items():

                if count == 3:
                    break

                name = datetime.strptime(
                    day,
                    "%Y-%m-%d"
                ).strftime("%a")

                forecast_text += (
                    f"» {name}: "
                    f"{round(value['min'])}°C ~ "
                    f"{round(value['max'])}°C "
                    f"({value['weather']})\n"
                )

                count += 1

            text = f"""
 ☀️ <b>ᴡᴇᴀᴛʜᴇʀ ɪɴ {city_name}, {state}, {country}</b>

 🌡️ ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ : <code>{temp}°C / {temp_f}°F</code>
 🤔 ғᴇᴇʟs ʟɪᴋᴇ : <code>{feels}°C / {feels_f}°F</code>
 ☁️ ᴄᴏɴᴅɪᴛɪᴏɴ : <code>{condition}</code>
 💧 ʜᴜᴍɪᴅɪᴛʏ : <code>{humidity}%</code>
 💨 ᴡɪɴᴅ : <code>{wind} km/h</code>
 👁️ ᴠɪsɪʙɪʟɪᴛʏ : <code>{visibility} km</code>
 ☀️ ᴜᴠ ɪɴᴅᴇx : <code>{uv} ({uv_text})</code>
 ☁️ ᴄʟᴏᴜᴅ ᴄᴏᴠᴇʀ : <code>{clouds}%</code>
 📊 ᴘʀᴇssᴜʀᴇ : <code>{pressure} mb</code>

 📅 <b>Fᴏʀᴇᴄᴀsᴛ:</b>
 {forecast_text}
 """

            await wait.delete()

            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ʀᴇғʀᴇsʜ •",
                            callback_data="weather_refresh"
                        ),
                        InlineKeyboardButton(
                            "• ᴜᴘᴅᴀᴛᴇs •",
                            url="https://t.me/Aero_Unity"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )

            await message.reply_text(
                text,
                parse_mode=ParseMode.HTML,
                reply_markup=buttons
            )

        except Exception as e:
            await wait.edit_text(
                f"❌ Error:\n{e}"
            )

    # ---------------- WEATHER REFRESH ---------------- #
    @bot.on_callback_query(filters.regex("^weather_refresh$"))
    async def weather_refresh(_, query):

        await query.answer(
            "Rᴇғʀᴇsʜɪɴɢ..."
        )
        city = WEATHER_CACHE.get(query.from_user.id)

        if not city:
            return await query.answer(
                "ᴡᴇᴀᴛʜᴇʀ ᴇxᴘɪʀᴇᴅ",
                show_alert=True
            )

        class FakeMessage:
            command = ["weather", city]
            text = f"/weather {city}"
            from_user = query.from_user

            async def reply_text(self, *args, **kwargs):
                return await query.message.reply_text(*args, **kwargs)

        await weather_cmd(_, FakeMessage())

    # ---------------- IMAGINE ---------------- #
    @bot.on_message(filters.command("imagine"))
    async def imagine(_, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "Usage:\n/imagine ʏᴏᴜʀ ᴛᴇxᴛ ᴏʀ ᴘʀᴏᴍᴘᴛ"
            )

        prompt = message.text.split(None, 1)[1]

        wait = await message.reply_text(
            "🎨 Gᴇɴᴇʀᴀᴛɪɴɢ Iᴍᴀɢᴇ...\n"
            "Pʟᴇᴀsᴇ Wᴀɪᴛ A Sᴇᴄ..."
        )
        try:
            url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

            img = requests.get(url, timeout=120)

            if img.status_code != 200:
                return await wait.edit_text(
                    "‼️ Fᴀɪʟᴇᴅ Tᴏ Gᴇɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇ , ᴛʀʏ ᴀɢᴀɪɴ."
                )

            file = "imagine.png"

            with open(file, "wb") as f:
                f.write(img.content)

            await wait.delete()

            await message.reply_photo(
                photo=file,
                caption=(
                    f"🎨 <b>Iᴍᴀɢᴇ Gᴇɴᴇʀᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ</b>\n"
                    " ʙʏ @Aero_Unity\n\n"
                    f"📝 <code>{prompt}</code>"
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• Rᴇɢᴇɴᴇʀᴀᴛᴇ •",
                                callback_data=f"regen_{prompt}"
                            ),
                            InlineKeyboardButton(
                                "• ᴄʟᴏsᴇ •",
                                callback_data="close_imagine"
                            )
                        ]
                    ]
                )
            )
            os.remove(file)

        except Exception as e:
            await wait.edit_text(
                f"❌ Error:\n{e}"
            )

    # ---------------- REGENERATE BUTTON ---------------- #
    @bot.on_callback_query(filters.regex("^regen_"))
    async def regenerate_image(_, query):

        prompt = query.data.replace("regen_", "")

        wait = await query.message.reply_text(
            "🔄 Rᴇɢᴇɴᴇʀᴀᴛɪɴɢ Iᴍᴀɢᴇ...\n"
            "Pʟᴇᴀsᴇ Wᴀɪᴛ..."
        )
        try:
            url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

            img = requests.get(url, timeout=120)

            if img.status_code != 200:
                return await wait.edit_text(
                    "‼️ Fᴀɪʟᴇᴅ Tᴏ Rᴇɢɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇ , ᴛʀʏ ᴀɢᴀɪɴ."
                )
            file = "regen.png"

            with open(file, "wb") as f:
                f.write(img.content)

            await wait.delete()

            await query.message.reply_photo(
                photo=file,
                caption=(
                    f"🎨 <b>Iᴍᴀɢᴇ Rᴇɢᴇɴᴇʀᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ</b>\n"
                    "ʙʏ @Aero_Unity\n\n"
                    f"📝 <code>{prompt}</code>"
                ),
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• Rᴇɢᴇɴᴇʀᴀᴛᴇ •",
                                callback_data=f"regen_{prompt}"
                            ),
                            InlineKeyboardButton(
                                "• ᴄʟᴏsᴇ •",
                                callback_data="close_imagine"
                            )
                        ]
                    ]
                )
            )
            os.remove(file)

        except Exception as e:
            await wait.edit_text(
                f"❌ Error:\n{e}"
            )

    # ---------------- CLOSE BUTTON ---------------- #
    @bot.on_callback_query(filters.regex("^close_imagine$"))
    async def close_imagine(_, query):

        try:
            await query.message.delete()
        except:
            pass

        await query.answer("• ᴄʟᴏsᴇᴅ • ✅️")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

    # ==========================================
    # FEEDBACK
    # ==========================================

    @bot.on_message(filters.command("feedback") & filters.private)
    async def feedback_cmd(client, message):

        keyboard = InlineKeyboardMarkup(
            [
                 [
                    InlineKeyboardButton(
                        "• Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ •",
                        url="https://t.me/Mr_Mohammed_29"
                    )
                 ],
                 [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close_feedback"
                    )
                 ]
            ]
        )

        await message.reply_photo(
            photo=FEEDBACK_IMAGE,
            caption=(
                "**Aɴʏ Fᴇᴇᴅʙᴀᴄᴋ**\n\n"
                "**- Fᴏᴜɴᴅ A Bᴜɢ?**\n"
                "**- Hᴀᴠᴇ A Sᴜɢɢᴇsᴛɪᴏɴ?**\n"
                "**- Nᴇᴇᴅ ʜᴇʟᴘ?**\n\n"
                "ᴄʟɪᴄᴋ **Contact Owner** Bᴇʟᴏᴡ."
            ),
            reply_markup=keyboard
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

    # ==========================================
    # CLOSE FEEDBACK
    # ==========================================

    @bot.on_callback_query(filters.regex("^close_feedback$"))
    async def close_feedback(client, query):

        await query.answer()

        try:
            await query.message.delete()
        except:
            pass

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

    # ==========================================
    # MAINTENANCE COMMAND
    # ==========================================
 
    @bot.on_message(filters.command("maintenance") & filters.private)
    async def maintenance_cmd(client, message):

        if message.from_user.id != OWNER_ID:
            return await message.reply_text(
                "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!</b>"
            )

        if len(message.command) < 2:

            status = "🟢 Eɴᴀʙʟᴇᴅ" if MAINTENANCE["enabled"] else "🔴 Dɪsᴀʙʟᴇᴅ"

            return await message.reply_text(
                f"""<b>Mᴀɪɴᴛᴇɴᴀɴᴄᴇ Pᴀɴɴᴇʟ</b>

    <b>• Sᴛᴀᴛᴜs :</b> {status}
    <b>• Rᴇᴀsᴏɴ :</b> <code>{MAINTENANCE["reason"]}</code>
 
    <b>Usage</b>
    /maintenance on Bot Updating...
    /maintenance off"""
            )

        args = message.text.split(maxsplit=2)
        mode = args[1].lower()

        if mode == "on":

            reason = "No reason provided"

            if len(args) >= 3:
                reason = args[2]

            MAINTENANCE["enabled"] = True
            MAINTENANCE["reason"] = reason

            await message.reply_text(
                f"""✅ <b>Mᴀɪɴᴛᴇɴᴀɴᴄᴇ Eɴᴀʙʟᴇᴅ</b>

    📝 <b>Rᴇᴀsᴏɴ</b> : <code>{reason}</code>"""
            )

        elif mode == "off":

            MAINTENANCE["enabled"] = False
            MAINTENANCE["reason"] = "No reason provided"

            await message.reply_text(
                "✅ <b>Mᴀɪɴᴛᴇɴᴀɴᴄᴇ Dɪsᴀʙʟᴇᴅ</b>"
            )

        else:

            await message.reply_text(
                "Usage:\n"
                "/maintenance on Bot Updating...\n"
                "/maintenance off"
            )


    # ==========================================
    # BLOCK USERS DURING MAINTENANCE
    # ==========================================

    @bot.on_message(filters.private, group=-100)
    async def maintenance_checker(client, message):

        if message.from_user.id == OWNER_ID:
            return

        if not MAINTENANCE["enabled"]:
            return

        await message.reply_text(
            f"""<b>Bᴏᴛ Uɴᴅᴇʀ Mᴀɪɴᴛᴇɴᴀɴᴄᴇ</b>

    • Bᴏᴛ Is Uᴘᴅᴀᴛɪɴɢ, Fɪxɪɴɢ Bᴜɢs, Eʀʀᴏʀs ᴀɴᴅ Aᴅᴅɪɴɢ Nᴇᴡ Fᴇᴀᴛᴜʀᴇs

    📝 <b>Rᴇᴀsᴏɴ</b> : <code>{MAINTENANCE["reason"]}</code>"""
        )

        raise StopPropagation

    # ==========================================
    # AI + OCR + PDF TOOLS
    # ==========================================

    gemini_client = None

    if GEMINI_API_KEY:
        gemini_client = genai.Client(
            api_key=GEMINI_API_KEY
        )


    AI_MODEL = "gemini-3.6-flash"
 
    # ==========================================
    # GEMINI HELPER
    # ==========================================

    async def gemini_text(prompt):

        if not gemini_client:
            raise Exception(
                "GEMINI_API_KEY is not configured."
            )

        response = await gemini_client.aio.models.generate_content(
            model=AI_MODEL,
            contents=prompt
        )

        if not response.text:
            raise Exception("AI returned an empty response.")

        return response.text.strip()

    # ==========================================
    # /SMARTNAME
    # ==========================================

    @bot.on_message(filters.command("smartname") & filters.private)
    async def smartname_cmd(client, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "🧠 <b>Sᴍᴀʀᴛ Nᴀᴍᴇ</b>\n\n"
                "Usage:\n"
                "<code>/smartname movie name</code>\n\n"
                "Eample:\n"
                "<code>/smartname Avengers Endgame 2019</code>",
                parse_mode=ParseMode.HTML
            )

        text = message.text.split(None, 1)[1].strip()

        wait = await message.reply_text(
            "🧠 <b>Cʀᴇᴀᴛɪɴɢ Sᴍᴀʀᴛ Fɪʟᴇɴᴀᴍᴇ...</b>",
            parse_mode=ParseMode.HTML
        )

        try:
            prompt = f"""
    Create a clean professional filename for this content:

    {text}

    Rules:
    - Keep the original meaning.
    - Remove unnecessary symbols.
    - Use a professional filename style.
    - Do not add an extension.
    - Return only the filename.
    """

            result = await gemini_text(prompt)

            result = result.replace("`", "").strip()

            await wait.edit_text(
                f"🧠 <b>Sᴍᴀʀᴛ Fɪʟᴇɴᴀᴍᴇ</b>\n\n"
                f"<code>{result}</code>",
                parse_mode=ParseMode.HTML
            )

        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:1000]}</code>",
                parse_mode=ParseMode.HTML
            )

    # ==========================================
    # /TRANSLATE
    # ==========================================

    @bot.on_message(filters.command("translate") & filters.private)
    async def translate_cmd(client, message):

        if len(message.command) < 3:
            return await message.reply_text(
                "🌍 <b>Tʀᴀɴsʟᴀᴛᴏʀ</b>\n\n"
                "Usage:\n"
                "<code>/translate language text</code>\n\n"
                "Example:\n"
                "<code>/translate Hindi Hello how are you?</code>",
                parse_mode=ParseMode.HTML
            )

        args = message.text.split(None, 2)

        language = args[1]
        text = args[2]

        wait = await message.reply_text(
            "🌍 <b>Tʀᴀɴsʟᴀᴛɪɴɢ...</b>",
            parse_mode=ParseMode.HTML
        )

        try:
            prompt = f"""
    Translate the following text into {language}.

    - Keep the meaning accurate and natural.
    - Return only the translated text.
    -  Text:
      {text}
    """

            result = await gemini_text(prompt)

            await wait.edit_text(
                f"🌍 <b>Tʀᴀɴsʟᴀᴛɪᴏɴ</b>\n\n"
                f"{result}",
                parse_mode=ParseMode.HTML
            )

        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:1000]}</code>",
                parse_mode=ParseMode.HTML
            )

    # ==========================================
    # /SUMMARIZE
    # ==========================================

    @bot.on_message(filters.command("summarize") & filters.private)
    async def summarize_cmd(client, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "📝 <b>Sᴜᴍᴍᴀʀɪᴢᴇ</b>\n\n"
                "Usage:\n"
                "<code>/summarize your text</code>",
                parse_mode=ParseMode.HTML
            )

        text = message.text.split(None, 1)[1].strip()

        wait = await message.reply_text(
            "📝 <b>Sᴜᴍᴍᴀʀɪᴢɪɴɢ...</b>",
            parse_mode=ParseMode.HTML
        ) 

        try:
            prompt = f"""
    Summarize the following text.

    Rules:
    - Keep the important information.
    - Remove unnecessary repetition.
    - Use simple language.
    - Use bullet points when useful.

    Text:
    {text}
    """

            result = await gemini_text(prompt)

            await wait.delete()

            for i in range(0, len(result), 4000):

                await message.reply_text(
                    result[i:i + 4000]
                )

        except Exception as e:
 
            await wait.edit_text(
                f"❌ <b>Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:1000]}</code>",
                parse_mode=ParseMode.HTML
            )
  
    # ==========================================
    # /GRAMMAR
    # ==========================================

    @bot.on_message(filters.command("grammar") & filters.private)
    async def grammar_cmd(client, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "✍️ <b>Gʀᴀᴍᴍᴀʀ Cʜᴇᴄᴋᴇʀ</b>\n\n"
                "Usage:\n"
                "<code>/grammar your sentence</code>",
                parse_mode=ParseMode.HTML
            )

        text = message.text.split(None, 1)[1].strip()

        wait = await message.reply_text(
            "✍️ <b>Cʜᴇᴄᴋɪɴɢ Gʀᴀᴍᴍᴀʀ...</b>",
            parse_mode=ParseMode.HTML
        )

        try:
            prompt = f"""
    Correct the grammar and spelling of this text.

    Rules:
    - Preserve the original meaning.
    - Make the English natural.
    - Return the corrected text first.
    - Then briefly list important corrections.

    Text:
    {text}
    """

            result = await gemini_text(prompt)

            await wait.delete()

            for i in range(0, len(result), 4000):

                await message.reply_text(
                    result[i:i + 4000]
                )

        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:1000]}</code>",
                parse_mode=ParseMode.HTML
            )

    # ==========================================
    # /CAPTIONAI
    # ==========================================

    @bot.on_message(filters.command("captionai") & filters.private)
    async def captionai_cmd(client, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "🎬 <b>Aɪ Cᴀᴘᴛɪᴏɴ Gᴇɴᴇʀᴀᴛᴏʀ</b>\n\n"
                "Usage:\n"
                "<code>/captionai movie name</code>",
                parse_mode=ParseMode.HTML
            )

        text = message.text.split(None, 1)[1].strip()

        wait = await message.reply_text(
            "🎬 <b>Gᴇɴᴇʀᴀᴛɪɴɢ Cᴀᴘᴛɪᴏɴ...</b>",
            parse_mode=ParseMode.HTML
        )
    
        try:
            prompt = f"""
    Create a professional Telegram movie/file caption.

    Content:
    {text}

    Include:
    • Title
    • Short description
    • Genre if known
    • Release year if known
    • Quality if provided
    • Audio/subtitle information if provided

    Do not invent information that is not provided.
    Use attractive but clean formatting.
    """

            result = await gemini_text(prompt)

            await wait.delete()

            for i in range(0, len(result), 4000):

                await message.reply_text(
                    result[i:i + 4000]
                )
   
        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:1000]}</code>",
                parse_mode=ParseMode.HTML
            )


    # ==========================================
    # /OCR
    # ==========================================

    @bot.on_message(
        filters.command("ocr") & filters.private
    )
    async def ocr_cmd(client, message):

        if not message.reply_to_message:
            return await message.reply_text(
                "🖼️ <b>Oᴄʀ</b>\n\n"
                "Reply to an image/photo with:\n"
                "<code>/ocr</code>",
                parse_mode=ParseMode.HTML
            )

        replied = message.reply_to_message

        if not replied.photo and not replied.document:
            return await message.reply_text(
                "❌ Pʟᴇᴀsᴇ Rᴇᴘʟʏ Tᴏ Aɴ Iᴍᴀɢᴇ."
            )

        wait = await message.reply_text(
            "🔎 <b>Exᴛʀᴀᴄᴛɪɴɢ Tᴇxᴛ...</b>",
            parse_mode=ParseMode.HTML
        )

        file_path = None

        try:

            file_path = await replied.download()

            with open(file_path, "rb") as f:
                image_bytes = f.read()

            mime_type = "image/jpeg"

            if file_path.lower().endswith(".png"):
                mime_type = "image/png"

            elif file_path.lower().endswith(".webp"):
                mime_type = "image/webp"

            image_part = types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type
            )

            response = await gemini_client.aio.models.generate_content(
                model=AI_MODEL,
                contents=[
                    image_part,
                    (
                        "Extract all readable text from this image. "
                        "Preserve the original wording as accurately "
                        "as possible. Return only the extracted text."
                    )
                ]
            )

            result = response.text

            if not result:
                return await wait.edit_text(
                    "❌ Nᴏ Rᴇᴀᴅᴀʙʟᴇ Tᴇxᴛ Fᴏᴜɴᴅ."
                )

            await wait.delete()

            for i in range(0, len(result), 4000):

                await message.reply_text(
                    result[i:i + 4000]
                )

        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Oᴄʀ Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:1000]}</code>",
                parse_mode=ParseMode.HTML
            )

        finally:

            if file_path and os.path.exists(file_path):

                try:
                    os.remove(file_path)
                except Exception:
                    pass

    # ==========================================
    # /PDF
    # ==========================================

    @bot.on_message(
        filters.command("pdf") & filters.private
    )
    async def pdf_cmd(client, message):

        if len(message.command) < 2:
            return await message.reply_text(
                "📄 <b>Pᴅғ Gᴇɴᴇʀᴀᴛᴏʀ</b>\n\n"
                "Usage:\n"
                "<code>/pdf Your text here</code>\n\n"
                "Example:\n"
                "<code>/pdf hii hello</code>",
                parse_mode=ParseMode.HTML
            )

        text = message.text.split(None, 1)[1].strip()

        wait = await message.reply_text(
            "📄 <b>Cʀᴇᴀᴛɪɴɢ Pᴅғ...</b>\n"
            "⏳ Pʟᴇᴀsᴇ ᴡᴀɪᴛ...",
            parse_mode=ParseMode.HTML
        )

        pdf_file = f"pdf_{message.from_user.id}.pdf"

        try:

            def create_pdf():

                from reportlab.lib.pagesizes import A4
                from reportlab.pdfgen import canvas
                from reportlab.pdfbase.pdfmetrics import stringWidth

                page_width, page_height = A4

                c = canvas.Canvas(
                    pdf_file,
                    pagesize=A4
                )

                c.setTitle("Generated PDF")

                margin_left = 50
                margin_right = 50
                margin_top = 50
                margin_bottom = 50

                max_width = (
                    page_width
                    - margin_left
                    - margin_right
                )

                font_name = "Helvetica"
                font_size = 12
                line_height = 18

                c.setFont(
                    font_name,
                    font_size
                )
  
                y = page_height - margin_top

                # Handle multiple lines
                paragraphs = text.splitlines()

                if not paragraphs:
                    paragraphs = [text]

                for paragraph in paragraphs:

                    words = paragraph.split()

                    # Empty line
                    if not words:
                        y -= line_height

                        if y < margin_bottom:
                            c.showPage()
                            c.setFont(
                                font_name,
                                font_size
                            )
                            y = page_height - margin_top

                        continue

                    line = ""

                    for word in words:

                       test_line = (
                           f"{line} {word}"
                       ).strip()

                       if stringWidth(
                           test_line,
                           font_name,
                           font_size
                       ) <= max_width:

                           line = test_line

                       else:

                           if line:

                               c.drawString(
                                   margin_left,
                                   y,
                                   line
                               )

                               y -= line_height

                           line = word

                           if y < margin_bottom:

                               c.showPage()

                               c.setFont(
                                   font_name,
                                   font_size
                               )

                               y = page_height - margin_top

                    if line:

                        c.drawString(
                            margin_left,
                            y,
                            line
                        )

                        y -= line_height

                    y -= 5

                    if y < margin_bottom:

                        c.showPage()

                        c.setFont(
                            font_name,
                            font_size
                        )

                        y = page_height - margin_top

                c.save()

            await asyncio.to_thread(
                create_pdf
            )

            # Make sure PDF actually exists
            if not os.path.exists(pdf_file):
                raise Exception(
                    "PDF file was not created."
                )

            if os.path.getsize(pdf_file) == 0:
                raise Exception(
                    "Generated PDF is empty."
                )

            await wait.delete()

            await message.reply_document(
                document=pdf_file,
                caption=(
                    "📄 <b>Pᴅғ Cʀᴇᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ</b>\n\n"
                    "📝 <b>Tᴇxᴛ:</b> "
                    f"<code>{text[:1000]}</code>"
                ),
                parse_mode=ParseMode.HTML
            )

        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Pᴅғ Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:1000]}</code>",
                parse_mode=ParseMode.HTML
            )

        finally:

            if os.path.exists(pdf_file):

                try:
                    os.remove(pdf_file)
                except Exception:
                    pass

    # ============================================================
    # MEDIA INFO HELPERS
    # ============================================================

    async def ffprobe_info(file_path):

        process = await asyncio.create_subprocess_exec(
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_streams",
            "-show_format",
            file_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )  

        stdout, stderr = await process.communicate()
  
        if process.returncode != 0:
            raise Exception(
                stderr.decode(errors="ignore")[-3000:]
            )

        return json.loads(
            stdout.decode(errors="ignore")
        )


    def get_replied_media(message):

        replied = message.reply_to_message

        if not replied:
            return False

        if replied.video:
            return True

        if replied.audio:
            return True

        if replied.document:
            mime = replied.document.mime_type or ""
 
            if (
                mime.startswith("video/")
                or mime.startswith("audio/")
                or mime == "application/octet-stream"
            ):
                return True

        return False

    # ============================================================
    # /AUDIOINFO
    # ============================================================

    @bot.on_message(
        filters.command("audioinfo") & filters.private
    )
    async def audioinfo_cmd(client, message):

        if not get_replied_media(message):
            return await message.reply_text(
                "🎵 <b>Aᴜᴅɪᴏ Iɴғᴏ</b>\n\n"
                "Reply to a video/audio file with:\n"
                "<code>/audioinfo</code>",
                parse_mode=ParseMode.HTML
            )

        wait = await message.reply_text(
            "🔍 <b>Rᴇᴀᴅɪɴɢ Aᴜᴅɪᴏ Iɴғᴏ...</b>",
            parse_mode=ParseMode.HTML
        )

        file_path = None

        try:

            file_path = await message.reply_to_message.download()

            info = await ffprobe_info(file_path)

            streams = info.get("streams", [])

            audios = [
                stream
                for stream in streams
                if stream.get("codec_type") == "audio"
            ]

            if not audios:
                return await wait.edit_text(
                    "❌ <b>Nᴏ Aᴜᴅɪᴏ Tʀᴀᴄᴋ Fᴏᴜɴᴅ.</b>",
                    parse_mode=ParseMode.HTML
                )

            text = "🎵 <b>Aᴜᴅɪᴏ Tʀᴀᴄᴋs</b>\n\n"

            for number, stream in enumerate(
                audios,
                start=1
            ):

                tags = stream.get("tags", {})

                language = tags.get(
                    "language",
                    "Unknown"
                )

                title = tags.get(
                    "title",
                    "Unknown"
                )

                codec = stream.get(
                    "codec_name",
                    "Unknown"
                )

                channels = stream.get(
                    "channels",
                    "Unknown"
                )

                bitrate = stream.get(
                    "bit_rate",
                    "Unknown"
                )

                if bitrate != "Unknown":

                    try:
                        bitrate = (
                            int(bitrate) // 1000
                        )
                        bitrate = f"{bitrate} kbps"
                    except:
                        pass

                text += (
                    f"🎧 <b>Track {number}</b>\n"
                    f"├ Language: "
                    f"<code>{language}</code>\n"
                    f"├ Name: "
                    f"<code>{title}</code>\n"
                    f"├ Codec: "
                    f"<code>{codec}</code>\n"
                    f"├ Channels: "
                    f"<code>{channels}</code>\n"
                    f"└ Bitrate: "
                    f"<code>{bitrate}</code>\n\n"
                )

            await wait.edit_text(
                text,
                parse_mode=ParseMode.HTML
            )

        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:2000]}</code>",
                parse_mode=ParseMode.HTML
            )

        finally:

            if file_path and os.path.exists(file_path):

                try:
                    os.remove(file_path)
                except:
                    pass

    # ============================================================
    # /SUBTITLEINFO
    # ============================================================

    @bot.on_message(
        filters.command("subtitleinfo") & filters.private
    )
    async def subtitleinfo_cmd(client, message):

        if not get_replied_media(message):
            return await message.reply_text(
                "💬 <b>Sᴜʙᴛɪᴛʟᴇ Iɴғᴏ</b>\n\n"
                "Reply to a video/file with:\n"
                "<code>/subtitleinfo</code>",
                parse_mode=ParseMode.HTML
            )

        wait = await message.reply_text(
            "🔍 <b>Rᴇᴀᴅɪɴɢ Sᴜʙᴛɪᴛʟᴇ Iɴғᴏ...</b>",
            parse_mode=ParseMode.HTML
        )

        file_path = None

        try:

            file_path = await message.reply_to_message.download()

            info = await ffprobe_info(file_path)

            streams = info.get("streams", [])

            subtitles = [
                stream
                for stream in streams
                if stream.get("codec_type") == "subtitle"
            ]

            if not subtitles:
                return await wait.edit_text(
                    "❌ <b>Nᴏ Sᴜʙᴛɪᴛʟᴇ Tʀᴀᴄᴋ Fᴏᴜɴᴅ.</b>",
                    parse_mode=ParseMode.HTML
                )

            text = "💬 <b>Sᴜʙᴛɪᴛʟᴇ Tʀᴀᴄᴋs</b>\n\n"

            for number, stream in enumerate(
                subtitles,
                start=1
            ):

                tags = stream.get("tags", {})

                language = tags.get(
                    "language",
                    "Unknown"
                )

                title = tags.get(
                    "title",
                    "Unknown"
                )

                codec = stream.get(
                    "codec_name",
                    "Unknown"
                )

                text += (
                    f"💬 <b>Track {number}</b>\n"
                    f"├ Language: "
                    f"<code>{language}</code>\n"
                    f"├ Name: "
                    f"<code>{title}</code>\n"
                    f"└ Codec: "
                    f"<code>{codec}</code>\n\n"
                )

            await wait.edit_text(
                text,
                parse_mode=ParseMode.HTML
            )

        except Exception as e:

            await wait.edit_text(
                f"❌ <b>Eʀʀᴏʀ</b>\n\n"
                f"<code>{str(e)[:2000]}</code>",
                parse_mode=ParseMode.HTML
            )

        finally:

            if file_path and os.path.exists(file_path):

                try:
                    os.remove(file_path)
                except:
                    pass  
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #