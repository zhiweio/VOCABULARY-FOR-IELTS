# VOCABULARY-FOR-IELTS

《雅思词汇真经》欧陆词典词库整理

## 资料

### 音频

[Bilibili - 雅思词汇真经】单词+例句带读](https://www.bilibili.com/video/BV1Tv4y1R7Gp/?p=1&t=633)

### 词库

[IELTS.eudic](./IELTS.eudic)

词库完成
- [x] Chapter 01
- [ ] Chapter 02
- [ ] Chapter 03
- [ ] Chapter 04
- [ ] Chapter 05
- [ ] Chapter 06
- [ ] Chapter 07
- [ ] Chapter 08
- [ ] Chapter 09
- [ ] Chapter 10
- [ ] Chapter 11
- [ ] Chapter 12
- [ ] Chapter 13
- [ ] Chapter 14
- [ ] Chapter 15
- [ ] Chapter 16
- [ ] Chapter 17
- [ ] Chapter 18
- [ ] Chapter 19
- [ ] Chapter 20
- [ ] Chapter 21
- [ ] Chapter 22

## 词库制作

### 生词本列表打印后的 HTML 转 Excel

```shell
$ ./eudic-cli.py excel print.html IELTS.xlsx -c 1
Found words              246
interpretations    246
phrases            246
examples           246
dtype: int64 words

```

### Excel 转 TXT

指定章节

```shell
$ ./eudic-cli.py txt IELTS.xlsx Chapter01/01.txt -c 1
```

全部章节

```shell
$ ./eudic-cli.py txt IELTS.xlsx IELTS.txt 
```

### TXT 格式说明

格式：
单词1@解释
单词2@解释
单词3@解释...
说明：

1. 每个单词解释一行，若解释中有换行，请替换为<br>
2. @为单词和解释的分隔符
3. 解释支持html格式
4. 支持解释内跳转 例如 <a href="dic://abc">test</a>

### TXT 转 eudic 词库

参照 [欧路词库编辑器](http://www.eudic.net/eudic/builder.aspx)
