from guizero import App, Text, PushButton, TextBox, TitleBox, ListBox, Combo, Window, Picture, Box
import guizero
from PIL import Image
import webbrowser
tC = "#ffffff"
bC = "#4a6da7"
gC = "#292929"
def main():
  A = App(title="JW Link Generator", width=600, height=800)
  A.bg = gC
  container = guizero.Box(A, align="top", width="fill")
  def open_jw_org():
    webbrowser.open("https://www.jw.org")
  def open_git():
    webbrowser.open("https://github.com/El-Flaco9/JW-Link-Generator")
  p = Picture(container, image="jw_logo.png", height=100, width=100, align="left")
  p.when_clicked = open_jw_org
  title_box = guizero.Box(container, align="right", width="fill")
  Text(title_box, text='JW Link Generator', size=30, color=tC, align="top")
  gen_icon = Picture(container, image="generated-icon.png",height=100, width=100, align="right")
  gen_icon.when_clicked = open_git
  Text(A, text="v1.0",size=10, color=tC)
  Text(A,text=" ",size=10, color=tC)
  Text(A, text="Enter Bible Book:",size=15, color=tC)
  def on_select(item):
    BOOK = item
  bible_books = {
      "Genesis": {"num":"01"},
      "Exodus": {"num":"02"},
      "Leviticus": {"num":"03"},
      "Numbers": {"num":"04"},
      "Deuteronomy": {"num":"05"},
      "Joshua": {"num":"06"},
      "Judges": {"num":"07"},
      "Ruth": {"num":"08"},
      "1 Samuel": {"num":"09"},
      "2 Samuel": {"num":"10"},
      "1 King": {"num":"11"},
      "2 King": {"num":"12"},
      "1 Chronicles":{"num":"13"},
      "2 Chronicles":{"num":"14"},
      "Ezra": {"num":"15"},
      "Nehemiah": {"num":"16"},
      "Esther": {"num":"17"},
      "Job": {"num":"18"},
      "Psalms": {"num":"19"},
      "Proverbs": {"num":"20"},
      "Ecclesiastes": {"num":"21"},
      "Song of Solomon": {"num":"22"},
      "Isaiah": {"num":"23"},
      "Jeremiah": {"num":"24"},
      "Lamentations": {"num":"25"},
      "Ezekiel": {"num":"26"},
      "Daniel": {"num":"27"},
      "Hosea": {"num":"28"},
      "Joel": {"num":"29"},
      "Amos": {"num":"30"},
      "Obadiah": {"num":"31"},
      "Jonah": {"num":"32"},
      "Micah": {"num":"33"},
      "Nahum": {"num":"34"},
      "Habakkuk": {"num":"35"},
      "Zephaniah": {"num":"36"},
      "Haggai": {"num":"37"},
      "Zechariah": {"num":"38"},
      "Malachi": {"num":"39"},
      "Matthew": {"num":"40"},
      "Mark": {"num":"41"},
      "Luke": {"num":"42"},
      "John": {"num":"43"},
      "Acts": {"num":"44"},
      "Romans": {"num":"45"},
      "1 Corinthians": {"num":"46"},
      "2 Corinthians": {"num":"47"},
      "Galatians": {"num":"48"},
      "Ephesians": {"num":"49"},
      "Philippians": {"num":"50"},
      "Colossians": {"num":"51"},
      "1 Thessalonians": {"num":"52"},
      "2 Thessalonians": {"num":"53"},
      "1 Timothy": {"num":"54"},
      "2 Timothy": {"num":"55"},
      "Titus": {"num":"56"},
      "Philemon": {"num":"57"},
      "Hebrews": {"num":"58"},
      "James": {"num":"59"},
      "1 Peter": {"num":"60"},
      "2 Peter": {"num":"61"},
      "1 John": {"num":"62"},
      "2 John": {"num":"63"},
      "3 John": {"num":"64"},
      "Jude": {"num":"65"},
      "Revelations": {"num":"66"}
  }
  books = ListBox(A, items=list(bible_books.keys()), scrollbar=True, command=on_select)
  books.bg = bC
  books.text_color = tC
  Text(A,text="Enter Book Chapter:",size=15, color=tC)
  CHAPTER = TextBox(A)
  CHAPTER.bg = bC
  CHAPTER.text_color = tC
  Text(A,text="Enter Chapter Verse:",size=15, color=tC)
  VERSE = TextBox(A)
  VERSE.bg = bC
  VERSE.text_color = tC
  Text(A,text="to",size=10, color=tC)
  T = TitleBox(A, text="Optional")
  T.text_color = tC
  TO_VERSE = TextBox(T)
  TO_VERSE.bg = bC
  TO_VERSE.text_color = tC
  Text(A,text="Choose Bible Edition:",size=15, color=tC)
  translations_list = {
      "New World Translation (2013)": {"link": "nwt","link_library": "nwt"},
      "New World Translation Study Edition": {"link": "study-bible","link_library": "nwtsty"},
      "King James Version": {"link": "king-james-version","link_library": "bi10"},
      "American Standard Version": {"link": "american-standard-version","link_library": "bi22"},
      "Emphasized Bible (Rotherham)": {"link": "rotherham","link_library": "rh"},
      "New World Translation (1984, also known as Reference Bible)": {"link": "bi12","link_library": "Rbi8"},
      "The Kingdom Interlinear Translation of the Greek Scriptures": {"link": "kingdom-interlinear-greek-translation","link_library": "int"},
      "The Bible in Living English": {"link": "byington","link_library": "by"}
  }
  edition = Combo(A, options=list(translations_list.keys()))
  edition.bg = bC
  edition.text_color = tC
  Text(A,text="Choose Language:",size=15, color=tC)
  lang = Combo(A, options=['English'])
  lang.bg = bC
  lang.text_color = tC
  Text(A,text=' ',size=10)
  def check_values():
      def errmsg(rsn):
          A.error("Error", text=rsn)
      if books.value == '':
          errmsg("Please select a book")
          return True
      elif CHAPTER.value == '':
          errmsg("Please enter a chapter")
          return True
      elif VERSE.value == '':
          errmsg("Please enter a verse")
          return True
      if not CHAPTER.value.isdigit():
          errmsg("Please enter a number for chapter")
          return True
      if not VERSE.value.isdigit():
          errmsg("Please enter a number for verse")
          return True
      if not TO_VERSE.value.isdigit():
          if TO_VERSE.value == '':
              return False
          else:
              errmsg("Please enter a number for to-verse")
              return True
  def generate_link():
    ED = ''
    cLink = ''
    vLink = ''
    global ER
    ER = False
    tLink= ''
    def errmsg(rsn):
        A.error("Error", text=rsn)
        global ER
        ER = True
    ER = check_values()
    link='https://www.jw.org/en/library/bible/'
    if edition.value in translations_list.keys():
        ED = translations_list[edition.value].get('link')
    else:
        errmsg("Translation is not available for JW.ORG")
        ER = True
    selected_book = books.value if books.value else ""
    selected_book = str(selected_book).lower()
    count = 1
    for i in bible_books:
      if i == books.value:
        break
      else:
        count += 1
    if len(str(CHAPTER.value)) == 2:
      cLink = "0" + str(CHAPTER.value)
    if len(str(CHAPTER.value)) == 1:
      cLink = "00" + str(CHAPTER.value)
    if len(str(VERSE.value)) == 2:
      vLink = "0" + str(VERSE.value)
    if len(str(VERSE.value)) == 1:
      vLink = "00" + str(VERSE.value)
    link = link + str(ED) + '/books/' + selected_book + '/' + str(CHAPTER.value) + '/#v' + str(count) + str(cLink) + str(vLink)
    if TO_VERSE.value != '':
      if TO_VERSE.value == str:
        errmsg("Please enter a number for To Verse")
      if len(str(TO_VERSE.value)) == 2:
        tLink = "0" + str(TO_VERSE.value)
      if len(str(TO_VERSE.value)) == 1:
        tLink = "00" + str(TO_VERSE.value)
      link = link + '-v' + str(count) + str(cLink) + str(tLink)
    if ER is False:
      W = Window(A, title="Generated Link", width=400, height=400)
      W.bg = gC
      Text(W, text="Generated Link", size=30, color=tC)
      l = TextBox(W, text=link, multiline=True, width=50, height=10, enabled=False)
      l.bg = bC
      l.text_color = tC
      def open_link(url):
        webbrowser.open(url)
      o = PushButton(W, text="Open", command=open_link, args=[link])
      o.bg = bC
      o.text_color = tC
    if ER is True:
        pass
  def generate_library_link():
      ED = ''
      cLink = ''
      vLink = ''
      TO_VERSE.value = ''
      global ER, bible_books_num
      ER = False
      ER = check_values()
      def errmsg(rsn):
          A.error("Error", text=rsn)
          global ER
          ER = True
      link = 'https://www.jw.org/finder?srcid=jwlshare&wtlocale=E&prefer=lang&bible='
      if edition.value in translations_list.keys():
          ED = translations_list[edition.value].get('link_library')
      else:
          errmsg("Translation is not available for JW Library")
          ER = True
      if len(str(CHAPTER.value)) == 2:
          cLink = "0" + str(CHAPTER.value)
      if len(str(CHAPTER.value)) == 1:
          cLink = "00" + str(CHAPTER.value)
      if len(str(VERSE.value)) == 2:
          vLink = "0" + str(VERSE.value)
      if len(str(VERSE.value)) == 1:
          vLink = "00" + str(VERSE.value)
      if books.value in bible_books.keys():
          bible_books_num = bible_books[books.value].get('num')
      else:
          errmsg("An unexpected error occurred, try selecting a book again")
          ER = True
      link = link + str(bible_books_num) + str(cLink) + str(vLink) + '&pub=' + str(ED)
      if ER is False:
          W = Window(A, title="Generated Link", width=400, height=400)
          W.bg = gC
          Text(W, text="Generated Link", size=30, color=tC)
          l = TextBox(W, text=link, multiline=True, width=50, height=10, enabled=False)
          l.bg = bC
          l.text_color = tC
          def open_link(url):
              webbrowser.open(url)
          o = PushButton(W, text="Open", command=open_link, args=[link])
          o.bg = bC
          o.text_color = tC
      if ER is True:
          print('err' + str(ER))
          pass
  gl = PushButton(A,text='Generate JW.ORG Link',padx=16,command=generate_link)
  gl.bg = bC
  gl.text_color = tC
  gll = PushButton(A,text='Generate JW Library Link',command=generate_library_link)
  gll.bg = bC
  gll.text_color = tC
  def example():
    books.value = "Revelations"
    CHAPTER.value = "21"
    VERSE.value = "3"
    TO_VERSE.value = "4"
    edition.value = "New World Translation Study Edition"
    lang.value = "English"
  ge = PushButton(A,text='Generate Example',padx=27,command=example)
  ge.bg = bC
  ge.text_color = tC
  A.display()

main()
