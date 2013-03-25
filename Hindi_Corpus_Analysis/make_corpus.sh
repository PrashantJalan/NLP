VAR="301"

for i in {1..20}
do

VAR=$((VAR+1))

FILE="/home/prashant/NLP/Hindi_Corpus_Analysis/hin_corp_unicode/"$VAR"_utf.txt"

cat $FILE >> /home/prashant/NLP/Hindi_Corpus_Analysis/corpus.txt

done
