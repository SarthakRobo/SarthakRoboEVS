import os

print("Final English Data setup ho raha hai...")

data = """Part 1: Word Meanings. आइए बच्चों, कुछ नए अंग्रेजी शब्दों के अर्थ सीखते हैं!
Sawaal 1.1. Stout (स्टाउट). बच्चों, स्टाउट का मतलब होता है बहुत मोटा और मजबूत। Answer: thick and firm
Sawaal 1.2. Secret (सीक्रेट). सीक्रेट का मतलब होता है कोई छुपी हुई बात या रहस्य। Answer: hidden
Sawaal 1.3. Disease (डिज़ीज़). डिज़ीज़ का मतलब होता है कोई बीमारी या रोग। Answer: an illness
Sawaal 1.4. Skeleton (स्केलेटन). स्केलेटन का मतलब है किसी जानवर या इंसान की हड्डियों का ढांचा। Answer: the bones of a whole animal or person
Sawaal 1.5. Greed (ग्रीड). ग्रीड का मतलब होता है लालच, यानी ज्यादा से ज्यादा पाने की इच्छा। Answer: a desire to have more and more
Sawaal 1.6. Wealth (वेल्थ). वेल्थ का मतलब होता है बहुत सारा पैसा और संपत्ति। Answer: riches
Sawaal 1.7. Curse (कर्स). कर्स का मतलब होता है किसी को श्राप या बद्दुआ देना। Answer: invoke misfortune
Sawaal 1.8. Solitude (सोलिट्यूड). सोलिट्यूड का मतलब है एकदम अकेलापन या एकांत। Answer: alone
Sawaal 1.9. Crawl (क्रॉल). क्रॉल का मतलब होता है धीरे-धीरे रेंगना, जैसे छोटे बच्चे चलते हैं। Answer: move slowly
Sawaal 1.10. Century (सेंचुरी). सेंचुरी का मतलब होता है पूरे 100 सालों का समय या शताब्दी। Answer: a period of 100 years
Sawaal 1.11. Voyages (वॉयजेस). वॉयजेस का मतलब है पानी के जहाज से की गई बहुत लंबी यात्रा। Answer: a long journey involving and planning
Sawaal 1.12. Carcasses (कारकासेस). कारकासेस का मतलब होता है किसी मरे हुए जानवर का शरीर। Answer: the dead body of animal
Sawaal 1.13. Reduced (रिड्यूस्ड). रिड्यूस्ड का मतलब होता है किसी चीज़ को कम कर देना। Answer: make smaller or less in amount
Sawaal 1.14. Virtual (वर्चुअल). वर्चुअल का मतलब है जो असली न हो, बल्कि कंप्यूटर से बनाया गया हो। Answer: made to appear with the help of a computer program
Sawaal 1.15. Magnificent (मैग्निफिसेंट). मैग्निफिसेंट का मतलब होता है बहुत ही शानदार और अद्भुत। Answer: wonderful
Sawaal 1.16. Amazement (अमेज़मेंट). अमेज़मेंट का मतलब होता है बहुत ज्यादा हैरानी की भावना। Answer: a feeling of great surprise
Sawaal 1.17. Bloom (ब्लूम). ब्लूम का मतलब है पौधों में सुंदर फूलों का खिलना। Answer: produce flowers
Sawaal 1.18. Diffused (डिफ्यूज़्ड). डिफ्यूज़्ड का मतलब होता है किसी चीज़ का बहुत दूर तक फैल जाना। Answer: spread widely
Sawaal 1.19. Arrayed (अरेड). अरेड का मतलब होता है किसी चीज़ को बहुत अच्छे तरीके से सजाकर रखना। Answer: arranged
Sawaal 1.20. Dear (डियर). डियर का मतलब है बहुत ही प्यारा या प्रिय। Answer: loving
Part 2: Multiple Choice Questions. चलिए बच्चों, अब हम सही विकल्प चुनते हैं!
Sawaal 2.1. The tree is... (पेड़ ... है।) तो बच्चों, हमने पढ़ा था कि पेड़ बड़ा और मजबूत दोनों होता है। इसलिए हमारा सही जवाब क्या होगा? दोनों! Answer: (c) both a and b
Sawaal 2.2. The tree holds _____ secret of children. (पेड़ बच्चों के _____ रहस्य रखता है।) कविता में कवि बताता है कि पेड़ अपने अंदर बच्चों के बहुत सारे, पूरे पचास राज छिपाकर रखता है। Answer: (a) fifty
Sawaal 2.3. The _____ of tree seem to touch the sky. (पेड़ की _____ आसमान को छूती हुई लगती हैं।) जब पेड़ बहुत बड़ा हो जाता है, तो उसकी जो डालियां होती हैं, वो इतनी ऊंची हो जाती हैं मानो आसमान को छू रही हों! Answer: (a) branches
Sawaal 2.4. The mother died only _____ days after the child was born. (बच्चे के जन्म के मात्र _____ दिन बाद माँ की मृत्यु हो गई।) यह कहानी राजकुमार सिद्धार्थ की है। उनके जन्म के केवल सात दिन बाद ही उनकी माता का देहांत हो गया था। Answer: (b) seven
Sawaal 2.5. The sickman was thrown out of the house because... (बीमार आदमी को घर से बाहर फेंक दिया गया था क्योंकि...) सिद्धार्थ ने जो बीमार आदमी देखा था, उसे घर से क्यों निकाला गया था? क्योंकि उसे एक बहुत ही भयंकर बीमारी हो गई थी। Answer: (c) he was suffering from terrible disease
Sawaal 2.6. Siddhartha became a _____ (सिद्धार्थ एक _____ बन गए।) राजमहल और सारी सुख-सुविधाएं छोड़ने के बाद, सच्चाई की खोज में सिद्धार्थ एक सन्यासी या तपस्वी बन गए थे। Answer: (c) hermit
Sawaal 2.7. The king was very fond of _____ (राजा को _____ का बहुत शौक था।) राजा मिडास को किस चीज़ से सबसे ज्यादा प्यार था? बिल्कुल सही, उसे सोना बहुत पसंद था! Answer: (c) gold
Sawaal 2.8. King Midas was very happy to get the power of _____ (राजा मिडास _____ की शक्ति पाकर बहुत खुश था।) राजा मिडास को जब यह जादुई शक्ति मिली कि वह जिस चीज़ को छुएगा वह सोने की हो जाएगी, तो वह खुशी से पागल हो गया था! Answer: (b) golden touch
Sawaal 2.9. The _____ turned into gold at the dining table. (डाइनिंग टेबल पर _____ सोने में बदल गए।) जब भूख लगने पर राजा मिडास खाना खाने बैठा, तो जैसे ही उसने ब्रेड और अंडे को छुआ, वो दोनों ही सोने के बन गए! Answer: (c) both (a) & (b)
Sawaal 2.10. The king did not want the golden touch anymore because... (राजा अब 'गोल्डन टच' नहीं चाहता था क्योंकि...) जब राजा की अपनी ही बेटी सोने की मूर्ति बन गई, तब उसे समझ आ गया कि उसका यह वरदान असल में एक श्राप बन गया है! Answer: (c) he understood that his wish had become a curse
Sawaal 2.11. At evening when the _____ is lit. (शाम को जब _____ जलाया जाता है।) कवि बताता है कि शाम के समय जब अंधेरा होने लगता है, तब घर में रोशनी के लिए लैंप जलाया जाता है। Answer: (c) lamp
Sawaal 2.12. In the story there were _____ (कहानी में _____ थे।) कवि जो कहानी पढ़ता है, उसमें सुंदर पहाड़ और घने जंगल दोनों ही होते हैं। Answer: (c) both a & b
Sawaal 2.13. The poet is an _____ (कवि एक _____ है।) बच्चों, इस कविता के कवि यूरोप से हैं, इसलिए उन्हें एक यूरोपियन कहा गया है। Answer: (b) European
Sawaal 2.14. In fifteenth century most people believed that the world was _____ (पंद्रहवीं सदी में ज्यादातर लोगों का मानना था कि दुनिया _____ है।) कोलंबस के समय में लोग सोचते थे कि हमारी धरती एकदम चपटी है! Answer: (b) flat
Sawaal 2.15. In August 1492, three small ships set sail from _____ (अगस्त 1492 में, तीन छोटे जहाज _____ से रवाना हुए।) दुनिया खोजने के लिए कोलंबस ने अपनी यात्रा स्पेन देश से शुरू की थी। Answer: (a) Spain
Sawaal 2.16. The Red Indians belonged to _____ (रेड इंडियंस _____ के रहने वाले थे।) जब कोलंबस अमेरिका पहुंचा, तो वहां रहने वाले मूल निवासियों को उसने गलती से 'रेड इंडियंस' कह दिया था। वो अमेरिका के ही रहने वाले थे। Answer: (b) America
Sawaal 2.17. In 1620, about a hundred _____ sailed from England in a ship. (1620 में, इंग्लैंड से लगभग एक सौ _____ एक जहाज में निकले।) नए देश अमेरिका में बसने के लिए जो पहला जहाज़ इंग्लैंड से निकला था, उसमें आदमी और औरतें दोनों शामिल थे। Answer: (c) both (a) & (b)
Sawaal 2.18. Merchants were going to a neighbouring kingdom for _____ (व्यापारी पड़ोसी राज्य में _____ के लिए जा रहे थे।) व्यापारी अपना सामान बेचने और व्यापार करने के लिए दूसरे राज्य जा रहे थे। Answer: (b) trading
Sawaal 2.19. All the leather containers were full of _____ (चमड़े के सभी बर्तन _____ से भरे हुए थे।) रेगिस्तान में पानी बहुत जरूरी होता है! इसलिए उन व्यापारियों ने अपने चमड़े के थैलों में पानी भर रखा था। Answer: (b) water
Sawaal 2.20. Soon the caravan entered the _____ (जल्द ही कारवां ने _____ में प्रवेश किया।) व्यापारियों का वह समूह चलते-चलते जल्द ही एक बहुत बड़े और सूखे रेगिस्तान में पहुंच गया। Answer: (a) desert
Sawaal 2.21. The young man told the headman that _____ (नौजवान ने मुखिया को बताया कि _____) उन बुरे लोगों ने मुखिया को बेवकूफ बनाने के लिए झूठ बोला था कि आगे रास्ते में एक बहुत बड़ा जंगल, झीलें और तालाब मिलेंगे। Answer: (c) they will see a big jungle, lakes and ponds
Sawaal 2.22. Rajan choose, the Taj Mahal at _____ (राजन ने _____ में स्थित ताजमहल को चुना।) दुनिया का मशहूर ताजमहल कहां है? जी हां, उत्तर प्रदेश के आगरा शहर में! Answer: (b) Agra
Sawaal 2.23. Ustad Ahmad Lahauri was the chief _____ (उस्ताद अहमद लाहौरी मुख्य _____ थे।) ताजमहल का नक्शा बनाने वाले मुख्य व्यक्ति उस्ताद अहमद लाहौरी थे। उन्हें हम वास्तुकार कहते हैं। Answer: (a) architect
Sawaal 2.24. The emperor built the Taj Mahal in the remembrance of his _____ (सम्राट ने ताजमहल अपनी _____ की याद में बनवाया था।) शाहजहां ने इतना सुंदर ताजमहल अपनी प्यारी पत्नी मुमताज की याद में बनवाया था। Answer: (c) wife
Sawaal 2.25. In a green and shady bed, a modest _____ grew. (एक हरे और छायादार जगह में, एक विनम्र _____ उगा।) कविता में हरी घास के बीच जो प्यारा और शर्मीला फूल खिला था, उसका नाम था वायलेट! Answer: (c) violet
Part 3: True or False. बच्चों, अब हम सही और गलत की पहचान करेंगे!
Sawaal 3.1. Trees give us shade and fresh air. (पेड़ हमें छाया और ताजी हवा देते हैं।) क्या पेड़ हमें ठंडी छांव और ताजी हवा देते हैं? बिल्कुल! इसलिए यह वाक्य एकदम सही है। Answer: True
Sawaal 3.2. Trees are useful only for making furniture. (पेड़ केवल फर्नीचर बनाने के लिए उपयोगी हैं।) क्या पेड़ सिर्फ फर्नीचर बनाने के काम आते हैं? नहीं बच्चों, पेड़ हमें मीठे फल, फूल, और बहुत कुछ देते हैं। तो यह बात गलत है! Answer: False
Sawaal 3.3. Birds can make their homes in trees. (पक्षी पेड़ों पर अपना घर बना सकते हैं।) क्या पक्षी पेड़ों पर अपना घोंसला बनाते हैं? बिल्कुल! पेड़ ही तो पक्षियों का घर है। यह बात सही है। Answer: True
Sawaal 3.4. A saint is generally known for a life of goodness and devotion. (एक संत को आम तौर पर अच्छाई और भक्ति के लिए जाना जाता है।) क्या एक संत या साधु अच्छे काम और भगवान की भक्ति के लिए जाने जाते हैं? हां, बिल्कुल! यह वाक्य सही है। Answer: True
Sawaal 3.5. The lesson teaches that kindness and good deeds have no value. (यह पाठ सिखाता है कि दया और अच्छे कामों की कोई कीमत नहीं है।) क्या अच्छे कामों की कोई कीमत नहीं होती? नहीं! अच्छे कामों की हमेशा बहुत कीमत होती है। यह गलत है। Answer: False
Sawaal 3.6. Respecting and helping others are good qualities. (दूसरों का सम्मान करना और मदद करना अच्छे गुण हैं।) क्या बड़ों की इज्जत करना और दूसरों की मदद करना अच्छी आदतें हैं? जी हां, यह बहुत ही अच्छी आदतें हैं। यह सही है। Answer: True
Sawaal 3.7. King Midas wished that everything he touched would turn into gold. (राजा मिडास ने कामना की थी कि वह जिस भी चीज़ को छुए, वह सोना बन जाए।) क्या लालची राजा मिडास ने भगवान से यही वरदान मांगा था? हां, बिल्कुल! यह सही है। Answer: True
Sawaal 3.8. Midas was completely happy with the golden touch from the beginning to the end. (मिडास शुरू से अंत तक 'गोल्डन टच' से पूरी तरह खुश था।) क्या राजा मिडास सोने का वरदान पाकर खुश था? नहीं! जब उसकी प्यारी बेटी सोने की बन गई तो वह बहुत दुखी था। इसलिए यह गलत है। Answer: False
Sawaal 3.9. The story teaches that love and family are more valuable than gold. (कहानी सिखाती है कि प्यार और परिवार सोने से ज्यादा मूल्यवान हैं।) क्या प्यार और हमारा परिवार सोने से ज्यादा कीमती हैं? हां बच्चों, यह बिल्कुल सही बात है! Answer: True
Sawaal 3.10. The poem celebrates the joy of reading story books. (कविता कहानी की किताबें पढ़ने की खुशी का जश्न मनाती है।) क्या यह कविता किताबें पढ़ने की खुशी के बारे में है? जी हां! किताबें पढ़ने में बहुत मज़ा आता है। यह सही है। Answer: True
Sawaal 3.11. Story books can take readers into wonderful imaginary worlds. (कहानी की किताबें पाठकों को अद्भुत काल्पनिक दुनिया में ले जा सकती हैं।) क्या कहानियां हमें परियों और जादुई दुनिया में ले जा सकती हैं? बिल्कुल ले जाती हैं! यह सही है। Answer: True
Sawaal 3.12. The poem says that children should never read books. (कविता कहती है कि बच्चों को कभी किताबें नहीं पढ़नी चाहिए।) क्या बच्चों को कभी किताबें नहीं पढ़नी चाहिए? अरे नहीं! किताबें तो हमें हमेशा पढ़नी चाहिए। यह बिल्कुल गलत है। Answer: False
Sawaal 3.13. Christopher Columbus is traditionally associated with the European voyage that reached the Americas in 1492. (कोलंबस 1492 में अमेरिका पहुंचने वाली यात्रा से जुड़े हैं।) क्या कोलंबस ने 1492 में अमेरिका तक की लंबी समुद्री यात्रा की थी? जी हां, यह बात बिल्कुल सही है। Answer: True
Sawaal 3.14. Columbus travelled across the Atlantic Ocean on his voyage. (कोलंबस ने अपनी यात्रा में अटलांटिक महासागर को पार किया था।) क्या कोलंबस ने अपनी यात्रा में अटलांटिक महासागर को पार किया था? हां बच्चों, यह सही है। Answer: True
Sawaal 3.15. The discovery story has nothing to do with ships or sea travel. (खोज की कहानी का जहाजों या समुद्री यात्रा से कोई लेना-देना नहीं है।) क्या अमेरिका की खोज में जहाज़ों का कोई काम नहीं था? यह तो बिल्कुल गलत है! वे जहाज़ से ही वहां पहुंचे थे। Answer: False
Sawaal 3.16. A wise leader thinks carefully before making importaint decisions. (एक बुद्धिमान नेता महत्वपूर्ण निर्णय लेने से पहले ध्यान से सोचता है।) क्या एक बुद्धिमान नेता कोई भी बड़ा फैसला लेने से पहले बहुत सोच-समझकर काम करता है? हां, बिल्कुल! यह सही है। Answer: True
Sawaal 3.17. A wise leader should listen to good advice. (एक बुद्धिमान नेता को अच्छी सलाह सुननी चाहिए।) क्या एक अच्छे लीडर को दूसरों की अच्छी सलाह सुननी चाहिए? जी हां, हमेशा सुननी चाहिए। यह सही है। Answer: True
Sawaal 3.18. The lesson presents foolishness as the most important quality of a leader. (पाठ मूर्खता को नेता के सबसे महत्वपूर्ण गुण के रूप में प्रस्तुत करता है।) क्या मूर्खता एक अच्छे लीडर की निशानी हो सकती है? कभी नहीं! लीडर तो समझदार होता है। यह गलत है। Answer: False
Sawaal 3.19. The Taj Mahal is a famous monument in Agra, India. (ताजमहल भारत के आगरा में एक प्रसिद्ध स्मारक है।) क्या ताजमहल भारत के आगरा शहर में बनी एक बहुत मशहूर ऐतिहासिक इमारत है? हां, यह पूरी दुनिया में मशहूर है! सही है। Answer: True
Sawaal 3.20. The Taj Mahal is made mainly of white marble. (ताजमहल मुख्य रूप से सफेद संगमरमर से बना है।) क्या ताजमहल सफेद संगमरमर से बना है? जी हां, यह चमकते हुए सफेद पत्थरों से बना है। सही है। Answer: True
Sawaal 3.21. A visit to a famous historical monument can help children learn about history and architecture. (किसी ऐतिहासिक स्मारक की यात्रा बच्चों को इतिहास जानने में मदद कर सकती है।) क्या ऐतिहासिक इमारत देखने से बच्चों को बहुत कुछ सीखने को मिलता है? बिल्कुल! सही है। Answer: True
Sawaal 3.22. A violet is a small flowering plant. (वायलेट एक छोटा फूल वाला पौधा है।) क्या वायलेट एक छोटा सा फूल देने वाला पौधा है? हां बच्चों, यह घास के बीच रहने वाला बहुत प्यारा पौधा होता है। सही है। Answer: True
Sawaal 3.23. The poem/story about the violet presents it as a beautiful flower. (वायलेट के बारे में कविता इसे एक खूबसूरत फूल के रूप में प्रस्तुत करती है।) क्या कविता में वायलेट को एक बहुत ही सुंदर और प्यारा फूल बताया गया है? बिल्कुल! यह सही है। Answer: True
Sawaal 3.24. The violet is described as a huge tree taller than a building. (वायलेट को एक इमारत से भी ऊंचे विशाल पेड़ के रूप में वर्णित किया गया है।) क्या वायलेट कोई बहुत बड़ा पेड़ है? अरे नहीं! वह तो जमीन पर उगने वाला एक छोटा सा पौधा है। यह गलत है। Answer: False
Sawaal 3.25. Flowers can add beauty to nature. (फूल प्रकृति की सुंदरता बढ़ा सकते हैं।) क्या फूल हमारी प्रकृति को और भी सुंदर बना देते हैं? जी हां, फूलों से ही तो दुनिया रंग-बिरंगी लगती है! यह बिल्कुल सही है। Answer: True
Part 4: Fill in the Blanks. बच्चों, अब हम खाली जगह में सही शब्द भरेंगे!
Sawaal 4.1. The king prayed to God to bless him with a _____. (राजा ने भगवान से प्रार्थना की कि उसे एक _____ का आशीर्वाद दें।) राजा के पास सब कुछ था, लेकिन उनकी एक ही इच्छा थी। उन्होंने प्रार्थना की थी कि उन्हें एक प्यारा सा बेटा मिल जाए। Answer: son
Sawaal 4.2. Siddhartha was brought up by his _____. (सिद्धार्थ का पालन-पोषण उनकी _____ ने किया था।) माता के देहांत के बाद सिद्धार्थ का पालन-पोषण किसने किया? उनकी मौसी यानी चाची ने उन्हें बड़े प्यार से पाला था। Answer: aunt
Sawaal 4.3. The people were happy to see their _____ prince. (लोग अपने _____ राजकुमार को देखकर खुश थे।) जब राजकुमार सिद्धार्थ नगर में निकले, तो लोग अपने सुंदर और आकर्षक राजकुमार को देखकर बहुत खुश हुए! Answer: charming
Sawaal 4.4. He saw an old man crying with _____. (उसने एक बूढ़े व्यक्ति को _____ से रोते हुए देखा।) सिद्धार्थ ने एक बीमार और बूढ़े आदमी को देखा। वह बूढ़ा आदमी बहुत ज्यादा दर्द से रो रहा था। Answer: pain
Sawaal 4.5. Sadhu looked _____ and happy. (साधु _____ और खुश लग रहा था।) सिद्धार्थ ने जब महल से बाहर एक साधु को देखा, तो वह साधु बहुत ही शांत और खुश दिखाई दे रहा था। Answer: peaceful
Sawaal 4.6. Siddhartha understood the _____ of life. (सिद्धार्थ को जीवन का _____ समझ में आ गया।) साधु को देखने के बाद सिद्धार्थ को जीवन का असली सच और रहस्य समझ आ गया था! Answer: secret
Sawaal 4.7. Columbus was an _____ from Genoa. (कोलंबस जेनोआ का रहने वाला एक _____ था।) कोलंबस इटली देश के जेनोआ का रहने वाला था। इसलिए कोलंबस एक इटैलियन था! Answer: Italian
Sawaal 4.8. Their bows pointed westwards across the wide unknown _____. (उनके जहाज़ों के अगले हिस्से पश्चिम की ओर विशाल अज्ञात _____ के पार इशारा कर रहे थे।) कोलंबस के जहाज़ों का मुंह पश्चिम दिशा की ओर अटलांटिक महासागर की तरफ था! Answer: Atlantic
Sawaal 4.9. The mainland of America was discovered by the _____. (अमेरिका की मुख्य भूमि की खोज _____ द्वारा की गई थी।) कोलंबस से भी पहले, अमेरिका की मुख्य भूमि की खोज नॉर्समैन नाम के बहादुर नाविकों ने की थी! Answer: Norsemen
Sawaal 4.10. Red Indians were the people who had _____ discovered America. (रेड इंडियंस वो लोग थे जिन्होंने सचमुच अमेरिका की खोज की थी।) असल में अमेरिका को सचमुच वहां पहले से रहने वाले रेड इंडियंस ने ही खोजा था। Answer: really
Sawaal 4.11. Things slowly _____. (चीजें धीरे-धीरे _____।) जब सफर में मुसीबत का समय बीतने लगा, तो हालात धीरे-धीरे सुधरने लगे थे। Answer: improved
Sawaal 4.12. They were carrying _____ water. (वे _____ पानी ले जा रहे थे।) रेगिस्तान के लंबे सफर के लिए, व्यापारियों के पास पीने के लिए पर्याप्त या काफी पानी था। Answer: sufficient
Sawaal 4.13. The old _____ was addressing his caravan. (बूढ़ा _____ अपने कारवां को संबोधित कर रहा था।) कारवां को उनका सबसे समझदार और बूढ़ा मुखिया समझा रहा था। Answer: headman
Sawaal 4.14. Their caravan was entering the _____. (उनका कारवां _____ में प्रवेश कर रहा था।) व्यापारियों का वह समूह रेत से भरे एक बहुत बड़े रेगिस्तान में प्रवेश कर रहा था। Answer: desert
Sawaal 4.15. The merchants were feeling _____. (व्यापारियों को _____ महसूस हो रहा था।) जब व्यापारियों को धोखे का पता चला, तो उन्हें बहुत ही बुरा लग रहा था। Answer: bad
Sawaal 4.16. The caravan was moving to its _____. (कारवां अपनी _____ की ओर बढ़ रहा था।) वह पूरा कारवां अपनी मंज़िल की तरफ बढ़ता जा रहा था। Answer: destination
Sawaal 4.17. Rajan collected the ticket and went towards a big _____. (राजन ने टिकट लिया और एक बड़े से _____ की ओर गया।) टिकट लेने के बाद राजन एक बहुत बड़े कमरे की तरफ गया था। Answer: room
Sawaal 4.18. He put his _____ on and fastened his seat belt. (उसने अपना _____ पहना और अपनी सीट बेल्ट बांध ली।) मशीन में सफर शुरू करने से पहले राजन ने सिर पर अपना हेलमेट पहना! Answer: helmet
Sawaal 4.19. Rajan was transported to a city _____ in Agra. (राजन को आगरा के एक शहर के _____ में पहुंचा दिया गया था।) मशीन चालू होते ही राजन आगरा शहर के एक चौराहे या चौक पर पहुंच गया था। Answer: square
Sawaal 4.20. Rajan looked very _____. (राजन बहुत _____ लग रहा था।) इतना सब कुछ नया और जादुई देखकर राजन बहुत ही ज्यादा उत्साहित लग रहा था! Answer: excited
Sawaal 4.21. The Taj Mahal shone like a _____. (ताजमहल एक _____ की तरह चमकता था।) सफेद संगमरमर से बना ताजमहल चांद की रोशनी में किसी रत्न की तरह चमक रहा था! Answer: jewel
Sawaal 4.22. The gardener is digging a _____. (माली एक _____ खोद रहा है।) माली नया पौधा लगाने के लिए ज़मीन में एक गड्ढा खोद रहा है। Answer: pit
Sawaal 4.23. Some monkeys have long _____. (कुछ बंदरों की लंबी _____ होती हैं।) आपने देखा ही होगा! कुछ बंदरों के पास बहुत लंबी पूंछ होती है। Answer: tails
Sawaal 4.24. Alka feeds the _____. (अल्का _____ को दाना खिलाती है।) अल्का नाम की बच्ची आंगन में आने वाली गौरैयों को दाना खिलाती है। Answer: sparrows
Part 5: Question & Answers. आइए बच्चों, अब हम कुछ मजेदार सवालों के जवाब देते हैं!
Sawaal 5.1. How will you come to know that tree is very tall? (आपको कैसे पता चलेगा कि पेड़ बहुत लंबा है?) जब हम किसी ऐसे पेड़ को देखते हैं जो बहुत बड़ा, तने से मोटा और मजबूत दिखे, तो हम समझ जाते हैं कि वह बहुत लंबा है! Answer: The tree that is big and stout and strong is very tall.
Sawaal 5.2. Which word of the poem shows that the tree is friendly? (कविता का कौन सा शब्द दर्शाता है कि पेड़ दोस्ताना है?) जब हम धूप में थक जाते हैं, तो पेड़ हमें अपनी ठंडी छांव देता है। यही शब्द बताता है कि पेड़ हमारा दोस्त है! Answer: The tree always let the poet to sit under his shade.
Sawaal 5.3. Who ruled over kapilavastu? (कपिलवस्तु पर किसने राज किया?) बच्चों, बहुत समय पहले कपिलवस्तु नाम के राज्य पर शाक्य वंश के राजाओं का राज हुआ करता था। Answer: The shakyas ruled over kapilvastu.
Sawaal 5.4. What did Siddhartha see in the town? (सिद्धार्थ ने नगर में क्या देखा?) जब राजकुमार सिद्धार्थ पहली बार महल से बाहर निकले, तो उन्होंने एक बीमार आदमी और एक मृत शरीर को देखा। Answer: Siddhartha saw a sick man and dead body in the town.
Sawaal 5.5. When did Siddhartha leave the palace? (सिद्धार्थ ने महल कब छोड़ा?) जीवन का असली सच जानने के लिए, उन्होंने एक बहुत ही अंधेरी रात को चुपचाप अपना महल छोड़ दिया था। Answer: Siddhartha left the palace in one dark night.
Sawaal 5.6. Who was king Midas? (राजा मिडास कौन था?) राजा मिडास प्राचीन यूनान की पुरानी कहानियों का एक बहुत ही लालची राजा था जिसे सोने से प्यार था। Answer: King Midas was an ancient Greek legend.
Sawaal 5.7. What happened to king Midas' daughter? (राजा मिडास की बेटी को क्या हुआ?) राजा ने जब गलती से अपनी प्यारी बेटी को छुआ, तो वह सोने की मूर्ति बन गई! Answer: King Midas' daughter turned into gold, when the king touched her.
Sawaal 5.8. Describe the way of spending poet's evening? (कवि की शाम बिताने के तरीके का वर्णन करें?) शाम के समय, कवि अपनी छोटी सी बंदूक के साथ खेलते हैं और जंगल के रास्तों पर घूमते हैं! Answer: In the evening the poet plays with his little gun and follow round the forest track.
Sawaal 5.9. How do the poet's parents spend their evening? (कवि के माता-पिता अपनी शाम कैसे बिताते हैं?) शाम को, कवि के माता-पिता आग के चारों ओर आराम से बैठकर बातें करते हैं और गीत गाते हैं। Answer: At evening the poet's parents would sit around the fire and talk and sing.
Sawaal 5.10. Who was Christopher Columbus? (क्रिस्टोफर कोलंबस कौन था?) वह इटली का रहने वाला एक बहुत ही महान समुद्री यात्री था, जो बाद में पुर्तगाल में रहने लगा था। Answer: Christopher Columbus was an Italian from Genoa living in Portugal.
Sawaal 5.11. Who were the first White men to settle in America? (अमेरिका में बसने वाले पहले श्वेत व्यक्ति कौन थे?) अमेरिका की खोज के बाद वहां बसने वाला सबसे पहला व्यक्ति अमेरिगो था! Answer: Amerigo was the first to settle in America.
Sawaal 5.12. What did the old headman ask before entering the desert? (रेगिस्तान में प्रवेश करने से पहले बूढ़े मुखिया ने क्या पूछा?) कारवां के रेगिस्तान में जाने से पहले बूढ़े मुखिया ने पूछा: 'क्या हमारे पास पीने के लिए पर्याप्त पानी है?' Answer: The old headman asked, "are we carrying sufficient water."
Sawaal 5.13. What did they see later on? (बाद में उन्होंने क्या देखा?) आगे जाकर उन्होंने देखा कि एक दूसरा कारवां मूर्ख बन गया था, और पानी खत्म हो जाने के कारण उन सब की मौत हो गई थी। Answer: They saw that the other caravan got fooled by same people and died because of shortage of water.
Sawaal 5.14. Who welcomed Rajan at the Taj Mahal? (ताजमहल में राजन का स्वागत किसने किया?) जब राजन ताजमहल देखने पहुंचे, तो वहां सोमनाथ नाम के एक नौजवान ने खुशी-खुशी उनका स्वागत किया। Answer: A young man named Somnath welcomed Rajan.
Sawaal 5.15. Why did shah Jahan build the taj mahal? (शाहजहां ने ताजमहल क्यों बनवाया था?) मुगल बादशाह शाहजहां ने अपनी प्यारी पत्नी मुमताज महल की याद में यह खूबसूरत इमारत बनवाई थी। Answer: Shah Jahan built this monument in the remembrance of his beloved wife Mumtaz Mahal.
Sawaal 5.16. Write two things that show the modesty of the violet? (वायलेट की विनम्रता को दर्शाने वाली दो बातें लिखिए?) वायलेट इतना शर्मीला है कि उसकी डंडी झुकी रहती है और वह अपना सिर नीचे लटकाए रखता है! Answer: Its stalk was bent and it hung its head, as if to hide from view."""

# Write to text file
with open("english_data.txt", "w", encoding="utf-8") as f:
    f.write(data.strip())

# Update HTML design and slides count
html_file = "templates/index.html"
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Badges and totals
html = html.replace("Testing | 5 Slides", "5 Parts | 115 Slides")
html = html.replace("totalSlides = 5;", "totalSlides = 115;")
html = html.replace("totalSlides = 5", "totalSlides = 115")

old_block = """            } else if (currentSubject === 'english') {
                addHeader("Part 1: Teacher Style Testing");
                for(let i=1; i<=5; i++) { addBtn(`1.${i}`, slideCounter++); }
            }"""

new_block = """            } else if (currentSubject === 'english') {
                const engParts = [ { title: "Word Meanings", count: 20 }, { title: "MCQs", count: 25 }, { title: "True/False", count: 25 }, { title: "Fill in Blanks", count: 24 }, { title: "Question Answers", count: 16 } ];
                engParts.forEach((part, index) => { addHeader(`Part ${index + 1}: ${part.title}`); addBtn("Intro", slideCounter++, true); for(let i=1; i<=part.count; i++) { addBtn(`${index + 1}.${i}`, slideCounter++); } });
            }"""

if "Part 1: Teacher Style Testing" in html:
    html = html.replace(old_block, new_block)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ English Data aur HTML Dashboard 115 Slides ke liye Update ho gaya!")
