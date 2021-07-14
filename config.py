# URLShortenerBot - A Telegram Bot To short long urls
#Copyright (C) 2021 by Rasak <https://github.com/Artis7eeR>
#URLShortenerBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#URLShortenerBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

def get_env(var):
  return os.environ.get(var,None)

class Config:
  BOT_TOKEN = get_env('BOT_TOKEN')
  
  START_TEXT = 'Hi, I am alive'
  
  HELP_TEXT = 'Send me a url to get shortened link'
  
  