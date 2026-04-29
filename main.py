# from tok_en import tk
# import asyncio 
# import logging 
# from aiogram import Dispatcher,Bot,F 
# import requests
# from aiogram.filters import CommandStart
# from aiogram.types import Message,CallbackQuery
# from inline_botton import menyu,menyubot, sonlar
# from qnopka import menyufunk
# dp = Dispatcher()
# bot = Bot(token=tk)
# logging.basicConfig(level=logging.INFO)

# response = requests.get(url = "https://fakeapi.pythonanywhere.com/products/").json()

# @dp.message(CommandStart()) 

# async def start(message:Message):
    
#     await message.answer("assalomu alaykum",reply_markup=menyu)
    
    
# @dp.callback_query(F.data == "menu") 
# async def Menuchiqar(cal:CallbackQuery):
#     await cal.message.answer_photo(photo="https://media.istockphoto.com/id/1428709516/photo/shopping-online-woman-hand-online-shopping-on-laptop-computer-with-virtual-graphic-icon.jpg?s=612x612&w=0&k=20&c=ROAncmFL4lbSQdU4VOhyXu-43ngzfEqHE5ZZAw5FtYk=",caption="hush kelibsiz",reply_markup=menyubot())
#     await cal.message.delete()

# @dp.callback_query(F.data == "orqaga1") 

# async def ortga(cal:CallbackQuery):
#     await cal.message.answer_photo(photo="https://media.istockphoto.com/id/1428709516/photo/shopping-online-woman-hand-online-shopping-on-laptop-computer-with-virtual-graphic-icon.jpg?s=612x612&w=0&k=20&c=ROAncmFL4lbSQdU4VOhyXu-43ngzfEqHE5ZZAw5FtYk=",caption="asosiy bolimga hush kelibsiz",reply_markup=menyubot())
#     await cal.message.delete()
    


# @dp.callback_query(F.data == "ortga") 

# async def ortga(cal:CallbackQuery):
#     await cal.message.answer("asosiy saxifaga hush kelibsiz",reply_markup=menyu)
#     await cal.message.delete()



# @dp.callback_query(F.data) 
# async def zakazbot(cal:CallbackQuery):
#     xabar = cal.data
#     if not xabar.isdigit(): 
#         for i in response:
#             if i["title"] == xabar:
#                 await cal.message.answer_photo(photo=i["image"],caption=f"Summa: {i["summ"]} som", reply_markup=sonlar()) 
#                 await cal.message.delete()
#                 break
                
#         else:
#             await cal.answer("maxsulot yoq")
#             await cal.message.delete()        
#     else:
#         await cal.answer("siz zaqas berdingiz bro",show_alert=True)


# async def main():
#     await dp.start_polling(bot) 

# if __name__ =="__main__":
#     try:
#         asyncio.run(main())

#     except: 
#         print("tugadi")  






# from aiogram import F,Dispatcher,Bot 
# import logging 
# import asyncio 
# from aiogram.filters import CommandStart  
# from aiogram.types import Message,callback_query,InputMediaPhoto
# from tok_en import tk
# from bottn import botton 
# from rasm import rasimlar

# dp = Dispatcher() 
# bot = Bot(token=tk)

# logging.basicConfig(level=logging.INFO)

# @dp.message()

# async def start(message:Message):
#     await message.answer_photo(photo=rasimlar[0] ,caption="bu juda ajoyib rasimlar",reply_markup=botton(count=0))   


# @dp.callback_query(F.data)
# async def funksiya(cal:callback_query):
    
    

#     xabar = cal.data.split("_")
#     count = int(xabar[-1])
#     if xabar[0] == "oldinga":
#         count+=1

#         await cal.message.edit_media(InputMediaPhoto(media=rasimlar[count],caption=f"bu rasimlardaki {count}"),reply_markup=botton(count=count)) 

#     elif xabar[0] == "ortga": 
#             count-=1
#             await cal.message.edit_media(InputMediaPhoto(media=rasimlar[count],caption=f"bu rasimlardaki {count}"),reply_markup=botton(count=count) )
#     else: 
#          await cal.answer(f"sizning buyurtmangiz{count}") 
#          await cal.message.delete()









# async def main():
#     await dp.start_polling(bot)



# if __name__ =="__main__":
#     try:
#         asyncio.run(main()) 

#     except:
#         print("toxtadi")    





                                                    # aiogram  


import os
import asyncio 
import logging 
from yt_dlp import YoutubeDL
from aiogram import Dispatcher,F,Bot 
from aiogram.types import Message,callback_query,FSInputFile
from aiogram.filters import CommandStart 
from tok_en import tk  
from bottn import menyu
from googletrans import Translator
from states import Form 
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
bot = Bot(token=tk)

@dp.message(CommandStart()) 

async def bottnbot(message:Message):
    await message.answer("salom menyudan tanlang", reply_markup=menyu)


@dp.callback_query(F.data == "translate") 

async def trans(cal:callback_query,state:FSMContext): 
    await cal.answer()
    await state.set_state(Form.translate) 
    await cal.message.answer("siz uzbekcha yozing men inglizcha qaytaraman", )

@dp.message(Form.translate) 

async def tarjima_handler(message: Message):
    tarjima = Translator()
    natija = await tarjima.translate(message.text,src="uz",dest="en")
    await message.answer(f"Tarjima: {natija.text}")


@dp.callback_query(F.data == "youtube") 

async def youtubestart(cal:callback_query,state:FSMContext):
    
    await state.set_state(Form.you_tube)  
    await cal.message.answer("siz you tubedan link yuboring men sizga sifatli vido tashlab beraman ") 


@dp.message(Form.you_tube) 

async def youtubedow(message:Message):
    link = message.text 
    videos = {"farmat": "mp4", "outtmpl": "video.(ext)%"}
    with YoutubeDL(videos) as dow: 
        dow.download(link)
    video = FSInputFile(f"video.mp4")    
    await message.answer_video(video=video)  
   
    os.remove('video.mp4')




    


 




async def main():
    await dp.start_polling(bot) 

if __name__ =="__main__":
    try:
        asyncio.run(main())
    except:
        print("toxtatildi")    
