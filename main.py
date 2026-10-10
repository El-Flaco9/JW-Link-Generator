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
  bible_books = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth", "1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy", "Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"]
  books = ListBox(A, items=bible_books, scrollbar=True, command=on_select)
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
      "New World Translation (2013)": {"link": "nwt"},
      "New World Translation Study Edition": {"link": "study-bible"},
      "King James Version": {"link": "king-james-version"},
      "American Standard Version": {"link": "american-standard-version"},
      "Emphasized Bible (Rotherham)": {"link": "rotherham"},
      "New World Translation (1984)": {"link": "bi12"},
      "The Kingdom Interlinear Translation of the Greek Scriptures": {"link": "kingdom-interlinear-greek-translation"},
      "The Bible in Living English": {"link": "byington"}
  }
  edition = Combo(A, options=list(translations_list.keys()))
  edition.bg = bC
  edition.text_color = tC
  Text(A,text="Choose Language:",size=15, color=tC)
  lang = Combo(A, options=['Local','English'])
  lang.bg = bC
  lang.text_color = tC
  Text(A,text=' ',size=10)
  def generate_link():
    ED = ''
    cLink = ''
    vLink = ''
    global ER
    ER = False
    tLink= ''
    def errmsg(rsn):
        A.error("Error",text=rsn)
        global ER
        ER = True
    if books.value == '':
      errmsg("Please select a book")
    elif CHAPTER.value == '':
      errmsg("Please enter a chapter")
    elif VERSE.value == '':
      errmsg("Please enter a verse")
    if not CHAPTER.value.isdigit():
        errmsg("Please enter a number for chapter")
    if not VERSE.value.isdigit():
        errmsg("Please enter a number for verse")
    if not TO_VERSE.value.isdigit():
        if TO_VERSE.value == '':
            pass
        else:
            errmsg("Please enter a number for to-verse")
    #elif edition.value == '':
    #  errmsg("Please select an edition")
    #elif lang.value == '':
    #  errmsg("Please select a language")
    link='https://www.jw.org/en/library/bible/'
    if edition.value in translations_list.keys():
        ED = translations_list[edition.value].get('link')
    else:
        errmsg("An unexpected error occurred, try to select a translation")
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
        print(str(ER))
        pass
  gl = PushButton(A,text='Generate JW.ORG Link',command=generate_link)
  gl.bg = bC
  gl.text_color = tC
  def example():
    books.value = "Revelation"
    CHAPTER.value = "21"
    VERSE.value = "3"
    TO_VERSE.value = "4"
    edition.value = "New World Translation Study Edition"
    lang.value = "Local"
  ge = PushButton(A,text='Generate Example',command=example)
  ge.bg = bC
  ge.text_color = tC
  A.display()

main()
