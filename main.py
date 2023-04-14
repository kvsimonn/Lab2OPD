import ttbot
if __name__ == '__main__':
    ttbot.executor.start_polling(ttbot.dp, skip_updates=True)