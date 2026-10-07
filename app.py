import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# आपका पूरा EVS डेटा (हेडिंग्स के साथ!)
evs_data = """
1. Multiple Choice Questions (MCQs) - बहुविकल्पीय प्रश्न

Sawaal 1.1. Which of the following carries blood from the heart? (इनमें से कौन हृदय से रक्त (खून) ले जाता है?)
बच्चों, हमारा दिल एक पंप की तरह काम करता है। जो नलियां इस पंप से साफ़ खून को हमारे पूरे शरीर तक ले जाती हैं, उन्हें हम धमनियां (arteries) कहते हैं। इसलिए सही जवाब है: (a) arteries (धमनियां)

Sawaal 1.2. The human body consists of _____________ bones. (मानव शरीर में _____________ हड्डियां होती हैं।)
क्या आपको पता है? एक बड़े इंसान के शरीर में कुल 206 हड्डियां होती हैं, जो मिलकर हमारे शरीर का ढांचा बनाती हैं। इसलिए सही जवाब है: (a) 206

Sawaal 1.3. The cerebrum is the largest part of the... (प्रमस्तिष्क (सेरेब्रम) किसका सबसे बड़ा हिस्सा है?)
हम जो कुछ भी सोचते हैं, याद रखते हैं या सीखते हैं, वो हमारे दिमाग (brain) के सबसे बड़े हिस्से की मदद से होता है, जिसे सेरेब्रम कहते हैं। इसलिए सही जवाब है: (b) brain (मस्तिष्क)

Sawaal 1.4. The liver produces a yellowish fluid called... (लिवर एक पीला तरल पदार्थ बनाता है जिसे ... कहते हैं।)
हमारा लिवर भारी खाने को पचाने के लिए एक पीले-हरे रंग का जूस बनाता है, जिसे पित्त (bile) कहा जाता है। इसलिए सही जवाब है: (a) bile (पित्त)

Sawaal 1.5. When you are born, you are a... (जब आपका जन्म होता है, point तो आप एक ... होते हैं।)
सोचो, जब हम इस दुनिया में आते हैं, तो हम क्या होते हैं? एक छोटे से प्यारे बच्चे! इसलिए सही जवाब है: (c) baby (बच्चे)

Sawaal 1.6. Plants grow from... (पौधे ... से उगते हैं।)
जब हम गमले की मिट्टी में छोटे-छोटे बीज बोते हैं, तो उन्हीं से सुंदर पौधे बाहर निकलते हैं। इसलिए सही जवाब है: (b) seeds (बीज)

Sawaal 1.7. Which of the following prepares food for plants? (इनमें से कौन पौधों के लिए भोजन तैयार करता है?)
पौधों का किचन उनकी हरी पत्तियां होती हैं। ये पत्तियां सूरज की रोशनी की मदद से पौधे के लिए खाना बनाती हैं। इसलिए सही जवाब है: (c) green leaves (हरी पत्तियां)

Sawaal 1.8. Fish swim with the help of... (मछलियां ... की मदद से तैरती हैं।)
मछलियों के पास हमारी तरह हाथ-पैर नहीं होते, इसलिए वे पानी में तैरने के लिए अपने पंखों (fins) का इस्तेमाल करती हैं। इसलिए सही जवाब है: (c) fins (पंख)

Sawaal 1.9. Plants and trees provide us with... (पौधे और पेड़ हमें ... देते हैं।)
पेड़-पौधे हमारे बहुत अच्छे दोस्त हैं। वे हमें फर्नीचर के लिए लकड़ी, खाने के लिए फल-सब्जियां और जानवरों के लिए चारा सब कुछ देते हैं। इसलिए सही जवाब है: (d) all of these (ये सभी)

Sawaal 1.10. Fruits and vegetables are rich sources of... (फल और सब्जियां ... के मुख्य स्रोत हैं।)
ताजे फलों और सब्जियों में हमें बीमारियों से बचाने वाले विटामिन्स और मजबूत बनाने वाले मिनरल्स (खनिज) दोनों भरपूर मात्रा में मिलते हैं। इसलिए सही जवाब है: (c) both of these (ये दोनों)

Sawaal 1.11. Tea is made from... (चाय ... से बनती है।)
सुबह-सुबह जो चाय हम पीते हैं, वह चाय के पौधों की हरी पत्तियों को तोड़कर और सुखाकर बनाई जाती है। इसलिए सही जवाब है: (b) leaves (पत्तियों)

Sawaal 1.12. Animals are the source of... (जानवर ... का स्रोत हैं।)
गाय-भैंस हमें पीने के लिए दूध देते हैं और मुर्गियों/बकरियों से हमें मांस मिलता है। इसलिए सही जवाब है: (d) both a and b (a और b दोनों)

Sawaal 1.13. In winters, we wear... (सर्दियों में, हम ... पहनते हैं।)
जब बहुत ठंड लगती है, तो हम खुद को गर्म रखने के लिए ऊन से बने स्वेटर और जैकेट पहनते हैं। इसलिए सही जवाब है: (c) woollen clothes (ऊनी कपड़े)

Sawaal 1.14. Which type of clothes should be wrapped in a cotton cloth before storing them? (किस तरह के कपड़ों को रखने से पहले सूती कपड़े में लपेटना चाहिए?)
रेशमी और ऊनी कपड़े बहुत नाज़ुक होते हैं और इनमें जल्दी कीड़े लग सकते हैं। इसलिए इन्हें हमेशा सूती कपड़े में लपेटकर सुरक्षित रखा जाता है। इसलिए सही जवाब है: (d) both a and b (a और b दोनों)

Sawaal 1.15. Jute is a... (जूट एक ... है।)
जूट हमें पौधों के तने से मिलता है, इसलिए यह प्रकृति से मिलने वाला एक प्राकृतिक रेशा (natural fibre) है जिससे बोरियां बनती हैं। इसलिए सही जवाब है: (a) natural fibre (प्राकृतिक रेशा)

Sawaal 1.16. We get wool from... (हमें ऊन ... से मिलती है।)
हमें गर्म ऊन सिर्फ भेड़ के बालों से ही नहीं, बल्कि ऊंट और याक जैसे जानवरों के बालों से भी मिलती है। इसलिए सही जवाब है: (d) both a and b (a और b दोनों)

Sawaal 1.17. Gypsies live in... (बंजारे (जिप्सी) ... में रहते हैं।)
बंजारे लोग एक जगह टिक कर नहीं रहते। वे पहियों पर बने घरों में रहते हैं, जिन्हें कारवां कहते हैं। इसलिए सही जवाब है: (a) caravans (कारवां/पहियों वाले घर)

Sawaal 1.18. Pucca houses are built of... (पक्के घर ... के बने होते हैं।)
पक्के घर बहुत मजबूत होते हैं क्योंकि उन्हें बनाने में सीमेंट, लोहे और ईंटों का इस्तेमाल होता है। इसलिए सही जवाब है: (d) bricks (ईंटों)

Sawaal 1.19. Kutcha houses are built of... (कच्चे घर ... के बने होते हैं।)
गांवों में जो कच्चे घर होते हैं, वे मिट्टी, गारे, बांस और भूसे से बनाए जाते हैं। इसलिए सही जवाब है: (b) mud (मिट्टी)

Sawaal 1.20. Eskimos live in... (एस्किमो ... में रहते हैं।)
जहां हमेशा बहुत बर्फ गिरती है, वहां लोग बर्फ के टुकड़ों से गोल घर बनाते हैं, जिन्हें इग्लू कहा जाता है। इसलिए सही जवाब है: (c) igloos (इग्लू/बर्फ के घर)

Sawaal 1.21. Air consists of... (हवा में ... होता है।)
हवा चाहे हमें दिखती नहीं, लेकिन यह जगह घेरती है इसलिए इसमें वजन (weight) होता है, और यह चीजों पर दबाव (pressure) भी डालती है। इसलिए सही जवाब है: (c) both of these (ये दोनों)

Sawaal 1.22. The gas needed for burning is... (जलने के लिए आवश्यक गैस ... है।)
अगर हवा में ऑक्सीजन गैस न हो, तो हम आग जला ही नहीं सकते! आग को जलने के लिए ऑक्सीजन बहुत ज़रूरी है। इसलिए सही जवाब है: (b) oxygen (ऑक्सीजन)

Sawaal 1.23. The layer of air that surrounds the earth is called the... (पृथ्वी के चारों ओर हवा की परत को ... कहा जाता है।)
हमारी पूरी पृथ्वी हवा की एक मोटी चादर से ढकी हुई है, और इस चादर को हम वायुमंडल कहते हैं। इसलिए सही जवाब है: (a) atmosphere (वायुमंडल)

Sawaal 1.24. Air contains... (हवा में शामिल है...)
हवा कोई एक चीज़ नहीं है! इसमें नाइट्रोजन, ऑक्सीजन, कार्बन डाइऑक्साइड गैसें और छोटे-छोटे धूल के कण भी मिले होते हैं। इसलिए सही जवाब है: (d) all of these (ये सभी)

Sawaal 1.25. Paints, fertilizers, and plastics are made from... (पेंट, खाद और प्लास्टिक ... से बनते हैं।)
ज़मीन के अंदर से जो गाढ़ा पेट्रोलियम निकलता है, उसी के रसायनों से पेंट, खेतों की खाद और प्लास्टिक की चीज़ें बनाई जाती हैं। इसलिए सही जवाब है: (a) petroleum (पेट्रोलियम)

Sawaal 1.26. Coal, petroleum, and natural gas are called... (कोयला, पेट्रोलियम और प्राकृतिक गैस को ... कहा जाता है।)
ये ज़मीन में दबे मरे हुए जीवों से हज़ारों सालों में बनते हैं (जीवाश्म ईंधन), और एक बार खत्म हो जाएं तो जल्दी दोबारा नहीं बनते (गैर-नवीकरणीय)। इसलिए सही जवाब है: (d) both a and c (a और c दोनों)

Sawaal 1.27. Solar energy is used in... (सौर ऊर्जा का उपयोग ... में किया जाता है।)
सूरज की गर्मी और धूप का इस्तेमाल हम सोलर कुकर में खाना पकाने और सोलर हीटर में पानी गर्म करने के लिए करते हैं। इसलिए सही जवाब है: (a) solar cookers (and solar heaters) (सोलर कुकर और हीटर में)

Sawaal 1.28. Which is the permanent source of all energy? (सभी ऊर्जा का स्थायी स्रोत कौन सा है?)
हमारी धरती पर ऊर्जा (energy) का सबसे बड़ा स्रोत जो कभी खत्म नहीं होगा, वह हमारा सूरज है। इसलिए सही जवाब है: (a) sun (सूर्य)

Sawaal 1.29. What causes the change in seasons? (मौसम में बदलाव का क्या कारण है?)
सर्दी, गर्मी और बरसात के मौसम इसलिए आते हैं क्योंकि हमारी पृथ्वी सूरज के चारों ओर पूरा चक्कर (परिक्रमण) लगाती है। इसलिए सही जवाब है: (a) revolution (परिक्रमण)

Sawaal 1.30. How many types of movements of the earth are there? (पृथ्वी की कितनी प्रकार की गतियां हैं?)
हमारी पृथ्वी दो तरह से घूमती है: पहला अपनी जगह पर लट्टू की तरह (Rotation) और दूसरा सूरज के चारों ओर (Revolution)। इसलिए सही जवाब है: (a) two (दो)

Sawaal 1.31. How many seasons are there? (कितने मौसम होते हैं?)
हमारे यहाँ मुख्य रूप से 4 तरह के मौसम आते हैं: गर्मी, सर्दी, पतझड़ और वसंत। इसलिए सही जवाब है: (a) four (चार - गर्मी, सर्दी, पतझड़, वसंत)

Sawaal 1.32. The equator is... (भूमध्य रेखा (इक्वेटर) एक ... है।)
पृथ्वी को दो बराबर हिस्सों में बांटने के लिए नक्शे पर बीचोबीच एक लाइन मानी गई है, यह सच में ज़मीन पर नहीं खिंची है! इसलिए सही जवाब है: (b) an imaginary line (काल्पनिक रेखा)

2. True or False (सही या गलत)

Sawaal 2.1. Kidneys work as blood purifiers. (गुर्दे खून साफ करने का काम करते हैं।)
बच्चों, हमारी किडनियां हमारे शरीर में एक छलनी (फिल्टर) की तरह काम करती हैं और खून से गंदे पदार्थों को साफ करती हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.2. The liver helps in digesting fatty foods. (लिवर वसायुक्त (फैट वाले) भोजन को पचाने में मदद करता है।)
जब हम तेल-घी वाला भारी खाना खाते हैं, तो हमारा लिवर एक खास रस बनाकर उसे पचाने में हमारी मदद करता है। इसलिए सही जवाब है: True (सही)

Sawaal 2.3. The brain is located near the stomach. (मस्तिष्क पेट के पास स्थित होता है।)
अरे नहीं! हमारा दिमाग तो हमारे शरीर के सबसे ऊपर, हमारे सिर के अंदर सुरक्षित रहता है, पेट के पास नहीं। इसलिए सही जवाब है: False (गलत)

Sawaal 2.4. The liver is the smallest organ in the human body. (लिवर मानव शरीर का सबसे छोटा अंग है।)
बिल्कुल गलत! लिवर तो हमारे शरीर के अंदर का सबसे बड़ा और भारी अंग होता है। इसलिए सही जवाब है: False (गलत)

Sawaal 2.5. Plants show movement. (पौधे गति दिखाते हैं।)
हाँ! पौधे अपनी जगह से चलकर तो नहीं जाते, लेकिन वे सूरज की रोशनी की तरफ अपनी पत्तियां और डालियां मोड़कर गति ज़रूर दिखाते हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.6. Non-living things can show movement when force is applied. (निर्जीव चीजें बल लगाने पर गति दिखा सकती हैं।)
बिल्कुल! अगर हम किसी रुकी हुई गाड़ी या गेंद (निर्जीव) को धक्का (बल) दें, तो वो आगे बढ़ने लगती है। इसलिए सही जवाब है: True (सही)

Sawaal 2.7. Plants develop throughout their lives. (पौधे जीवन भर विकसित होते हैं।)
हाँ बच्चों, पेड़-पौधे अपने पूरे जीवन में लगातार बढ़ते रहते हैं और उनमें नई पत्तियां और शाखाएं आती रहती हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.8. Plants do not show reproduction. (पौधे प्रजनन (अपने जैसे नए पौधे बनाना) नहीं करते हैं।)
यह गलत है। पौधे अपने बीजों से बिल्कुल अपने जैसे नए छोटे पौधे पैदा करते हैं, जिसे प्रजनन कहते हैं। इसलिए सही जवाब है: False (गलत)

Sawaal 2.9. All natural things have life. (सभी प्राकृतिक चीजों में जीवन होता है।)
नहीं बच्चों! पहाड़, नदियां और पत्थर भी प्राकृतिक हैं, लेकिन उनमें जान (जीवन) नहीं होती। इसलिए सही जवाब है: False (गलत)

Sawaal 2.10. Vegetables are not eaten in their natural forms. (सब्जियों को उनके प्राकृतिक रूप में नहीं खाया जाता है।)
यह गलत है! हम गाजर, मूली, टमाटर और खीरा जैसी सब्ज़ियों को बिना पकाए (कच्चा) उनके प्राकृतिक रूप में ही तो खाते हैं। इसलिए सही जवाब है: False (गलत)

Sawaal 2.11. Plants provide vegetables. (पौधे हमें सब्जियां देते हैं।)
हाँ! हमें आलू, गोभी, भिंडी जैसी सारी ताज़ी सब्जियां पौधों से ही तो मिलती हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.12. Animals give us milk and meat. (जानवर हमें दूध और मांस देते हैं।)
बिल्कुल सही! गाय, भैंस और बकरी से हमें दूध मिलता है, और मुर्गियों से मांस मिलता है। इसलिए सही जवाब है: True (सही)

Sawaal 2.13. Pulses are good for health. (दालें स्वास्थ्य के लिए अच्छी होती हैं।)
हाँ बच्चों, दालों में बहुत सारा प्रोटीन होता है जो हमारे शरीर को मजबूत बनाता है। इसलिए सही जवाब है: True (सही)

Sawaal 2.14. In winter, we wear cotton clothes. (स सर्दियों में, हम सूती कपड़े पहनते हैं।)
अरे नहीं! सर्दियों में तो हम खुद को गर्म रखने के लिए ऊनी (woollen) कपड़े पहनते हैं, सूती नहीं। इसलिए सही जवाब है: False (गलत)

Sawaal 2.15. Clothes are made from natural fibres only. (कपड़े केवल प्राकृतिक रेशों से बनते हैं।)
नहीं, कपड़े इंसान द्वारा बनाए गए कृत्रिम रेशों (जैसे नायलॉन और पॉलिएस्टर) से भी बनते हैं, सिर्फ प्राकृतिक रेशों से नहीं। इसलिए सही जवाब है: False (गलत)

Sawaal 2.16. People who weave clothes are called weavers. (कपड़े बुनने वाले लोगों को बुनकर (weavers) कहा जाता है।)
हाँ! जो लोग धागों से सुंदर कपड़े बुनने का काम करते हैं, उन्हें हम बुनकर ही कहते हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.17. We get synthetic fibres from petroleum. (हमें पेट्रोलियम से कृत्रिम रेशे (सिंथेटिक फाइबर) मिलते हैं।)
बिल्कुल! नायलॉन जैसे कृत्रिम रेशे ज़मीन से निकलने वाले पेट्रोलियम के रसायनों से ही फैक्ट्रियों में बनाए जाते हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.18. Bungalows are big, attractive, and cheap. (बंगले बड़े, आकर्षक और सस्ते होते हैं।)
बंगले बड़े और बहुत सुंदर तो होते हैं, लेकिन उन्हें बनाने में बहुत पैसा लगता है, वे सस्ते नहीं होते। इसलिए सही जवाब है: False (गलत - सस्ते नहीं होते)

Sawaal 2.19. Flats have several houses built one above the other in a single building. (फ्लैट्स में एक ही इमारत में एक के ऊपर एक कई घर बने होते हैं।)
हाँ, शहरों में जो ऊंची-ऊंची इमारतें होती हैं, उनमें जगह बचाने के लिए एक के ऊपर एक बहुत सारे घर (फ्लैट्स) बनाए जाते हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.20. Tents serve only as a hiding place for a short period of time. (तंबू (टेंट) केवल थोड़े समय के लिए छिपने या रहने की जगह के रूप में काम करते हैं।)
बिल्कुल, टेंट कपड़े के बने घर होते हैं जिन्हें हम कैंपिंग करते समय बस कुछ दिनों के लिए लगाते हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.21. A caravan moves on wheels. (एक कारवां पहियों पर चलता है।)
हाँ! कारवां एक ऐसा चलता-फिरता घर होता जिसके नीचे पहिये लगे होते हैं, ताकि लोग इसे कहीं भी ले जा सकें। इसलिए सही जवाब है: True (सही)

Sawaal 2.22. The earth is surrounded by an atmospheric layer. (पृथ्वी एक वायुमंडलीय परत से घिरी हुई है।)
बिल्कुल! हमारी पूरी पृथ्वी के चारों तरफ हवा का एक बहुत बड़ा घेरा है, जिसे वायुमंडल कहते हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.23. Most plants use nitrogen directly from the air. (ज्यादातर पौधे सीधे हवा से नाइट्रोजन का उपयोग करते हैं।)
नहीं बच्चों, पौधे हवा में मौजूद नाइट्रोजन को सीधे नहीं ले सकते। वे इसे अपनी जड़ों के ज़रिए मिट्टी से सोखते हैं। इसलिए सही जवाब है: False (गलत - वे मिट्टी से लेते हैं)

Sawaal 2.24. Sound vibrations do not travel in the air. (ध्वनि के कंपन (आवाज़) हवा में यात्रा नहीं करते हैं।)
यह गलत है। जब हम बोलते हैं, तो आवाज़ हवा के ज़रिए ही तो उड़कर हमारे कानों तक पहुँचती है! इसलिए सही जवाब है: False (गलत - करते हैं)

Sawaal 2.25. We can feel air. (हम हवा को महसूस कर सकते हैं।)
हाँ! जब तेज़ पंखा चलता है या बाहर हवा चलती है, तो हम अपनी त्वचा पर हवा को महसूस कर सकते हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.26. Minerals are man-made resources. (खनिज मानव निर्मित संसाधन हैं।)
नहीं, खनिज (जैसे लोहा, सोना, कोयला) ज़मीन के अंदर प्राकृतिक रूप से पाए जाते हैं, इंसान इन्हें नहीं बनाता। इसलिए सही जवाब है: False (गलत)

Sawaal 2.27. Coal is a fossil fuel. (कोयला एक जीवाश्म ईंधन है।)
बिल्कुल! कोयला ज़मीन के अंदर दबे मरे हुए पेड़-पौधों के जीवाश्मों से हज़ारों सालों में बनता है। इसलिए सही जवाब है: True (सही)

Sawaal 2.28. Natural resources are limited in supply. (प्राकृतिक संसाधन सीमित मात्रा में हैं।)
हाँ बच्चों, कोयला और पेट्रोल जैसी चीज़ें अगर हम बहुत ज़्यादा इस्तेमाल करेंगे तो वो एक दिन खत्म हो जाएंगी, इसलिए ये सीमित हैं। इसलिए सही जवाब है: True (सही)

Sawaal 2.29. Petroleum is a renewable resource. (पेट्रोलियम एक नवीकरणीय संसाधन (जो कभी खत्म न हो) है।)
नहीं! पेट्रोलियम बनने में लाखों साल लगते हैं। अगर यह एक बार खत्म हो गया, तो जल्दी दोबारा नहीं बनेगा। इसलिए सही जवाब है: False (गलत)

Sawaal 2.30. The earth does not move. (पृथ्वी नहीं घूमती है।)
अरे, यह तो बिल्कुल गलत है! हमारी पृथ्वी सूरज के चारों ओर भी घूमती है और अपनी जगह पर लट्टू की तरह भी घूमती रहती है। इसलिए सही जवाब है: False (गलत)

Sawaal 2.31. The revolution of the earth causes day and night. (पृथ्वी के परिक्रमण (सूर्य के चारों ओर घूमने) से दिन और रात होते हैं।)
नहीं बच्चों, दिन और रात पृथ्वी के अपनी जगह (धुरी) पर लट्टू की तरह घूमने (घूर्णन) से होते हैं, सूर्य के चक्कर लगाने से नहीं। इसलिए सही जवाब है: False (गलत - घूर्णन से होते हैं)

Sawaal 2.32. The revolution of the earth takes 24 hours. (पृथ्वी को परिक्रमण (सूर्य का चक्कर लगाने) में 24 घंटे लगते हैं।)
नहीं! पृथ्वी को अपनी जगह पर घूमने में 24 घंटे लगते हैं, लेकिन सूरज का पूरा चक्कर लगाने (परिक्रमण) में पूरे 365 दिन (1 साल) लगते हैं। इसलिए सही जवाब है: False (गलत - 1 साल लगता है)

Sawaal 2.33. Seasons are caused due to the revolution of the earth. (मौसम में बदलाव पृथ्वी के परिक्रमण (सूर्य के चारों ओर घूमने) के कारण होता है।)
हाँ! जब पृथ्वी सूरज का चक्कर लगाती है, तो सूरज से उसकी दूरी और झुकाव बदलने के कारण ही सर्दी और गर्मी के मौसम आते हैं। इसलिए सही जवाब है: True (सही)

3. Fill in the Blanks (खाली स्थान भरें)

Sawaal 3.1. The brain requires a continuous supply of blood and _________. (मस्तिष्क को रक्त और _________ की निरंतर आपूर्ति की आवश्यकता होती है।)
बच्चों, हमारे दिमाग को बिना रुके काम करने के लिए खून के साथ-साथ ताज़ी ऑक्सीजन गैस की भी लगातार ज़रूरत होती है। इसलिए सही जवाब है: oxygen

Sawaal 3.2. Our heart is as large as a _________. (हमारा हृदय एक _________ के जितना बड़ा होता है।)
ज़रा अपनी मुट्ठी बांधकर देखो! हमारा दिल भी बिल्कुल हमारी एक बंद मुट्ठी के आकार का ही होता है। इसलिए सही जवाब है: fist

Sawaal 3.3. The liver is _________ shaped. (लिवर _________ के आकार का होता है।)
हमारे लिवर का आकार एक त्रिकोण या कील (wedge) के टुकड़े जैसा होता है। इसलिए सही जवाब है: wedge

Sawaal 3.4. The liver is known as the chemical _________. (लिवर को रसायन (केमिकल) का _________ कहा जाता है।)
लिवर हमारे शरीर के अंदर बहुत सारे ज़रूरी रसायन (केमिकल्स) बनाता है, इसलिए इसे शरीर की केमिकल फैक्ट्री कहा जाता है। इसलिए सही जवाब है: factory

Sawaal 3.5. Non-living things do not possess _________. (निर्जीव चीजों में _________ नहीं होता है।)
कुर्सी, टेबल या पत्थर जैसी निर्जीव चीजों में जान या जीवन (life) नहीं होता, इसलिए वे सांस नहीं लेते। इसलिए सही जवाब है: life

Sawaal 3.6. Animals breathe with the help of a _________. (जानवर _________ की मदद से सांस लेते हैं।)
ज़्यादातर जानवर बिल्कुल हमारी तरह ही अपनी नाक से हवा अंदर खींचकर सांस लेते हैं। इसलिए सही जवाब है: nose

Sawaal 3.7. _________ is the process of making food by plants. (_________ पौधों द्वारा भोजन बनाने की प्रक्रिया है।)
पौधे जो सूरज की रोशनी में अपना खाना खुद बनाते हैं, उस शानदार प्रक्रिया को प्रकाश संश्लेषण (Photosynthesis) कहते हैं। इसलिए सही जवाब है: Photosynthesis

Sawaal 3.8. Leaves usually tend to move towards the _________. (पत्तियां आमतौर पर _________ की ओर बढ़ती हैं।)
पौधों को खाना बनाने के लिए धूप चाहिए होती है, इसलिए उनकी पत्तियां हमेशा सूरज की रोशनी की तरफ मुड़ जाती हैं। इसलिए सही जवाब है: sunlight

Sawaal 3.9. Plants _________ during the course of their lives. (पौधे अपने पूरे जीवन में _________ हैं।)
पौधे एक छोटे बीज से शुरू होकर एक बड़ा पेड़ बन जाते हैं, यानी वो जीवन भर बढ़ते (grow) रहते हैं। इसलिए सही जवाब है: grow

Sawaal 3.10. Eggs are very _________. (अंडे बहुत _________ होते हैं।)
अंडों में शरीर को ताक़त देने वाला प्रोटीन बहुत अधिक मात्रा में होता है, इसलिए वे बहुत पौष्टिक होते हैं। इसलिए सही जवाब है: nutritious

Sawaal 3.11. Animals and plants are important for our _________ needs. (जानवर और पौधे हमारी _________ की जरूरतों के लिए महत्वपूर्ण हैं।)
हमें फल-सब्ज़ियां पौधों से और दूध जानवरों से मिलता है, यानी ये हमारी भोजन की ज़रूरतें पूरी करते हैं। इसलिए सही जवाब है: food

Sawaal 3.12. _________ are major components of our daily food. (_________ हमारे दैनिक भोजन का मुख्य हिस्सा हैं।)
हम रोज़ रोटी और चावल के साथ दालें ज़रूर खाते हैं, क्योंकि ये हमें बहुत ताक़त देती हैं। इसलिए सही जवाब है: Pulses

Sawaal 3.13. Overcooking spoils the _________ present in food. (ज्यादा पकाने से भोजन में मौजूद _________ नष्ट हो जाते हैं।)
अगर हम सब्ज़ियों को बहुत ज़्यादा देर तक पका दें, तो उनमें मौजूद विटामिन्स खत्म हो जाते हैं। इसलिए सही जवाब है: vitamins

Sawaal 3.14. Cotton is obtained from _________ plants. (कपास (कॉटन) _________ के पौधों से प्राप्त होता है।)
हमारे सूती कपड़े बनाने वाली रूई हमें कपास (cotton) के पौधों से ही मिलती है। इसलिए सही जवाब है: cotton

Sawaal 3.15. Silk is a _________ fibre. (रेशम एक _________ रेशा है।)
रेशम हमें रेशम के कीड़ों से मिलता है, जो प्रकृति का हिस्सा हैं, इसलिए यह एक प्राकृतिक रेशा है। इसलिए सही जवाब है: natural

Sawaal 3.16. Nylon is a _________ fibre. (नायलॉन एक _________ रेशा है।)
नायलॉन इंसान द्वारा फैक्ट्रियों में रसायनों से बनाया जाता है, इसलिए यह कृत्रिम (synthetic) रेशा है। इसलिए सही जवाब है: synthetic

Sawaal 3.17. We get wool from _________. (हमें _________ से ऊन मिलती है।)
हमें सर्दियों से बचाने वाली गर्म ऊन भेड़ के बालों को काटकर मिलती है। इसलिए सही जवाब है: sheep

4. Answer the Following Questions (प्रश्नों के उत्तर दें)

Sawaal 4.1. Where is the brain situated? (मस्तिष्क कहाँ स्थित होता है?)
बच्चों, हमारा दिमाग बहुत नाज़ुक होता है, इसलिए यह हमारे शरीर के सबसे ऊपरी हिस्से यानी हमारे सिर की मजबूत हड्डियों के अंदर सुरक्षित रहता है। इसलिए सही जवाब है: The brain is situated in the uppermost part of the body, inside the head.

Sawaal 4.2. Which is the largest internal organ in the body? (शरीर का सबसे बड़ा आंतरिक (अंदर का) अंग कौन सा है?)
हमारे शरीर के अंदर कई सारे अंग होते हैं, लेकिन उनमें सबसे बड़ा और भारी अंग हमारा लिवर होता है। इसलिए सही जवाब है: The liver is the largest internal organ of the human body.

Sawaal 4.3. Why is the heart considered important? (हृदय को महत्वपूर्ण क्यों माना जाता है?)
हमारा दिल हमारे शरीर का सबसे ज़रूरी पंप है। यह बिना रुके लगातार काम करता है और खून के ज़रिए पूरे शरीर और दिमाग तक ऑक्सीजन और ताक़त पहुँचाता है। इसलिए सही जवाब है: The heart is considered important because it supplies blood to the body. It is responsible for the continuous flow of blood throughout the body and brain.

Sawaal 4.4. What is the function of the brain? (मस्तिष्क का क्या कार्य है?)
दिमाग हमारे शरीर का बॉस (controller) होता है! यह तय करता है कि हम कब चलें, क्या बोलें, और यहाँ तक कि हमारे दिल की धड़कन और सांस को भी यही कंट्रोल करता है। इसलिए सही जवाब है: The brain is the controller of the body. It commands the functioning of every part of the body, controls the heartbeat and breathing, and directs every movement.

Sawaal 4.5. What is the function of the lungs? (फेफड़ों का क्या कार्य है?)
हमारे फेफड़े गुब्बारों की तरह होते हैं। जब हम हवा अंदर खींचते हैं, तो ये फूल जाते हैं और हमें सांस लेने में मदद करते हैं। इसलिए सही जवाब है: The major function of the lungs is respiration (breathing).

Sawaal 4.6. What is the function of the liver? (लिवर का क्या कार्य है?)
लिवर हमारे शरीर की भट्टी की तरह है जो हमारे शरीर को गर्म रखता है, और यह भारी खाने (घी-तेल) को पचाने के लिए एक खास रस (पित्त) बनाता है। इसलिए सही जवाब है: The liver helps in maintaining a constant body temperature. It produces bile juice, which helps in the digestion of fatty foods.

Sawaal 4.7. What is the function of the kidneys? (गुर्दों (किडनी) का क्या कार्य है?)
किडनियां हमारे शरीर में छलनी (filter) का काम करती हैं। ये हमारे खून से गंदे पानी को छानकर अलग कर देती हैं, जो पेशाब (urine) के रूप में शरीर से बाहर निकल जाता है। इसलिए सही जवाब है: The process of excretion takes place with the help of the kidneys. Blood and water are filtered through the kidneys. The excess water passes into the ureter, where it goes into the bladder as urine.

Sawaal 4.8. What are the features of living and non-living things? (सजीव और निर्जीव चीजों की क्या विशेषताएं हैं?)
सजीव चीजें (जैसे हम और जानवर) हिल सकती हैं, बढ़ती हैं, सांस लेती हैं और उन्हें भूख लगती है। लेकिन निर्जीव चीजें (जैसे पत्थर या मेज़) न तो सांस लेती हैं, न बढ़ती हैं और न ही बच्चे पैदा करती हैं। इसलिए सही जवाब है: Living things show movement, grow, breathe, need food for growth, have feelings, and reproduce. Non-living things do not grow, breathe, or reproduce.

Sawaal 4.9. Write about the process of movement in animals. (जानवरों में गति की प्रक्रिया के बारे में लिखिए।)
दुनिया के सारे सजीव प्राणी हिल-डुल सकते हैं। ज़्यादातर जानवर अपने पैरों से चलते हैं, और जिन मछलियों के पैर नहीं होते, वो पानी में अपने पंखों (fins) से तैरती हैं। इसलिए सही जवाब है: All living things show the characteristic of movement. Most land animals move with the help of their legs. Since fish do not possess legs, they swim with the help of their fins.

Sawaal 4.10. How do plants produce their food? (पौधे अपना भोजन कैसे बनाते हैं?)
पौधे अपना खाना किसी किचन में नहीं बनाते। वे सूरज की रोशनी, हवा, पानी और पत्तियों में मौजूद हरे रंग (क्लोरोफिल) का जादुई इस्तेमाल करके अपना खाना बनाते हैं जिसे प्रकाश संश्लेषण कहते हैं। इसलिए सही जवाब है: Plants produce their own food using water, air, sunlight, and a green pigment called chlorophyll present in their leaves. This process is known as photosynthesis.

Sawaal 4.11. Do plants show feelings? Explain. (क्या पौधे भावनाएं दिखाते हैं? स्पष्ट करें।)
बच्चों, पौधों के पास हमारी तरह आंख-कान नहीं होते, फिर भी अगर आप 'छुईमुई' के पौधे को छूओगे, तो वो शरमाकर अपनी पत्तियां बंद कर लेता है। इसका मतलब वो महसूस कर सकते हैं! इसलिए सही जवाब है: Plants do not have sense organs like humans, yet they react to their surroundings. For example, the leaves of the 'touch-me-not' plant close as soon as we touch them.

Sawaal 4.12. Write three differences between living and non-living things. (सजीव और निर्जीव चीजों के बीच तीन अंतर लिखिए।)
सजीव (Living): 1) वे समय के साथ बड़े होते हैं, 2) बच्चे पैदा करते हैं, 3) अपने आप चल सकते हैं। निर्जीव (Non-living): ये तीनों काम नहीं कर सकते! इसलिए सही जवाब है:
Living Things: 1) They grow. 2) They reproduce. 3) They can move on their own.
Non-living Things: 1) They do not grow. 2) They do not reproduce. 3) They cannot move on their own.

Sawaal 4.13. What are the sources of food? (भोजन के स्रोत क्या हैं?)
हमें खाना मुख्य रूप से दो जगहों से मिलता है: पेड़-पौधों से (अनाज, फल, सब्जियां, दालें) और जानवरों से (दूध, अंडे, मांस)। इसलिए सही जवाब है: The main sources of food are plants and animals. Plants provide us with food grains, fruits, vegetables, beverages, oils, pulses, and spices. Animals provide us with milk, eggs, and meat.

Sawaal 4.14. Name some seafoods. (कुछ समुद्री भोजन (seafoods) के नाम बताइए।)
समुद्र से मिलने वाले खाने में झींगा, केकड़े और कई तरह की मछलियां शामिल होती हैं। इसलिए सही जवाब है: Prawns, crabs, and fish are examples of seafood.

Sawaal 4.15. Which animals provide us with milk and meat? (कौन से जानवर हमें दूध और मांस देते हैं?)
गाय, भैंस और बकरियां हमें पीने के लिए ताकतवर दूध देती हैं, और मुर्गी, मछली आदि से हमें मांस मिलता है। इसलिए सही जवाब है: We get milk from cows, buffaloes, and goats. We get meat from goats, hens, fish, etc.

Sawaal 4.16. What is another name for bayleaf? (तेजपत्ता (bayleaf) का दूसरा नाम क्या है?)
सब्ज़ी में खुशबू बढ़ाने के लिए डलने वाले तेज़पत्ते को हम तेज़ पत्ता या 'करी पत्ता' भी कहते हैं। इसलिए सही जवाब है: Bayleaf is also called Tej Patta or Kari Patta.

Sawaal 4.17. What clothes did early men wear? (आदिमानव कौन से कपड़े पहनते थे?)
पुराने समय में जब कपड़े बनाने की मशीनें नहीं थीं, तब इंसान जानवरों की खाल, पेड़ों की छाल और बड़ी-बड़ी पत्तियों को कपड़ों की तरह पहनते थे। इसलिए सही जवाब है: Early men wore clothes made from the skin of animals. They also used the bark of trees and large leaves to cover themselves.

Sawaal 4.18. What are synthetic fibres? (कृत्रिम रेशे (Synthetic fibres) क्या हैं?)
जो रेशे पेड़-पौधों से नहीं बल्कि फैक्ट्रियों में रसायनों से इंसान द्वारा बनाए जाते हैं, उन्हें कृत्रिम रेशे कहते हैं। ये बहुत मज़बूत होते हैं, जैसे नायलॉन। इसलिए सही जवाब है: Synthetic fibres are man-made fibres created from chemicals. They last longer than natural fibres. Examples include nylon and polyester.

Sawaal 4.19. How should we take care of silk and woollen clothes? (हमें रेशमी और ऊनी कपड़ों की देखभाल कैसे करनी चाहिए?)
रेशमी और ऊनी कपड़ों को कीड़ों से बचाने के लिए, उन्हें हमेशा सूती कपड़े में लपेटकर और उनके साथ सूखी नीम की पत्तियां या फिनाइल की गोलियां रखनी चाहिए। इसलिए सही जवाब है: We should wrap silk and woollen clothes in a cotton cloth and store them with dried neem leaves or naphthalene balls to protect them from insects.

Sawaal 4.20. What are the main raw materials for making clothes? (कपड़े बनाने के लिए मुख्य कच्चा माल क्या है?)
कपड़े या तो सीधे प्रकृति से मिलने वाले रेशों (जैसे रूई या ऊन) से बनते हैं या फिर फैक्ट्रियों में बने कृत्रिम रेशों (जैसे नायलॉन) से। इसलिए सही जवाब है: Clothes are made from either natural fibres (like cotton and wool) or synthetic fibres (like nylon).

Sawaal 4.21. Define movable houses. Give an example. (चलने-फिरने वाले घरों (Movable houses) की परिभाषा दें। एक उदाहरण दें।)
जो घर ज़मीन से जुड़े नहीं होते और जिन्हें आसानी से एक जगह से दूसरी जगह ले जाया जा सकता है (जैसे कारवां या नाव पर बना घर), उन्हें मूवेबल हाउस कहते हैं। इसलिए सही जवाब है: Movable houses are temporary houses that can be easily moved from one place to another. Examples include houseboats and caravans.

Sawaal 4.22. What is a permanent house? (स्थायी घर (Permanent house) क्या है?)
जो घर एक ही जगह पर ईंट, पत्थर, लोहे और सीमेंट से मजबूती से बनाए जाते हैं और जिन्हें हिलाया नहीं जा सकता, उन्हें पक्का घर कहते हैं। इसलिए सही जवाब है: A house constructed with strong materials like steel, bricks, concrete, and metal is called a permanent house or pucca house.

Sawaal 4.23. What kind of roof does an igloo have? (इग्लू की छत कैसी होती है?)
इग्लू की छत गोल और गुंबद जैसी होती है, जिसे लोग कठोर बर्फ के टुकड़ों को एक के ऊपर एक रखकर बनाते हैं। इसलिए सही जवाब है: An igloo has a round, dome-shaped roof made up of blocks of hard snow.

Sawaal 4.24. Why do houses in hilly areas have sloping roofs? (पहाड़ी इलाकों में घरों की छतें ढलान वाली क्यों होती हैं?)
पहाड़ों पर बहुत बारिश और बर्फबारी होती है। ढलान वाली छत होने से पानी और बर्फ छत पर रुकते नहीं, बल्कि आसानी से नीचे फिसल जाते हैं। इसलिए सही जवाब है: Houses in hilly areas have sloping roofs because these areas face heavy rainfall and snowfall. Sloping roofs allow the water and snow to slide down easily.

Sawaal 4.25. How can you prove air occupies space? (आप कैसे साबित कर सकते हैं कि हवा जगह घेरती है?)
एक खाली गुब्बारा लो और उसमें हवा भरो, वह फूलकर बड़ा हो जाएगा। इससे साफ पता चलता है कि हवा अंदर जाकर जगह घेर रही है! इसलिए सही जवाब है: We can prove that air occupies space with a simple activity: Blow air into a balloon and hold the top tight. The balloon becomes larger as air fills into it. This proves that air occupies space.

Sawaal 4.26. How can you prove air exerts pressure? (आप कैसे साबित कर सकते हैं कि हवा दबाव डालती है?)
अगर हम पानी से भरे गिलास के मुंह पर एक गत्ता रखकर गिलास को उल्टा कर दें, तो गत्ता नीचे नहीं गिरता क्योंकि नीचे से हवा उस पर ऊपर की ओर दबाव डालती है। इसलिए सही जवाब है: Fill a glass with water up to the brim. Press a piece of stiff cardboard tightly over the mouth of the glass. Quickly invert the glass and remove your hand slowly from the cardboard. The cardboard does not fall because the air from outside presses it upwards. This proves air exerts pressure.

Sawaal 4.27. What exactly is air? (हवा वास्तव में क्या है?)
हवा हमारे लिए बहुत ज़रूरी है! यह सिर्फ एक गैस नहीं, बल्कि कई गैसों, पानी की भाप और छोटे-छोटे धूल के कणों का एक बड़ा मिश्रण है। इसलिए सही जवाब है: Air is an important natural resource. It is a mixture of many gases, water vapour, and dust particles.

Sawaal 4.28. Which are the most prevalent gases in the air? (हवा में सबसे अधिक मात्रा में कौन सी गैसें पाई जाती हैं?)
हमारे आस-पास की हवा में सबसे ज़्यादा नाइट्रोजन (78%) और ऑक्सीजन (21%) गैसें होती हैं। इसलिए सही जवाब है: The main gases in the air are nitrogen (78%) and oxygen (21%).

Sawaal 4.29. What are renewable resources? (नवीकरणीय संसाधन (Renewable resources) क्या हैं?)
प्रकृति की वो चीज़ें जो हम रोज़ इस्तेमाल करते हैं फिर भी वो खत्म नहीं होतीं, जैसे सूरज की धूप, हवा और पानी, उन्हें नवीकरणीय संसाधन कहते हैं। इसलिए सही जवाब है: Renewable resources are natural resources that do not get exhausted even after continuous use. They can be naturally replenished. Examples include sunlight, wind, and water.

Sawaal 4.30. What are non-renewable resources? (गैर-नवीकरणीय संसाधन (Non-renewable resources) क्या हैं?)
वो चीज़ें जो एक बार इस्तेमाल होने के बाद हमेशा के लिए खत्म हो जाती हैं और दोबारा नहीं बन सकतीं (जैसे कोयला और पेट्रोल), उन्हें गैर-नवीकरणीय संसाधन कहते हैं। इसलिए सही जवाब है: Resources that cannot be easily replaced or recycled once used are called non-renewable resources. Examples include coal and petroleum.

Sawaal 4.31. What are the uses of water? (पानी के क्या उपयोग हैं?)
हम सुबह उठने से लेकर रात तक पानी का इस्तेमाल पीने, नहाने, सफाई करने और खेतों में सिंचाई करने के लिए करते हैं। इसलिए सही जवाब है: We need water for various daily activities like drinking, cooking, cleaning, bathing, and for agriculture.

Sawaal 4.32. How is electricity produced from water? (पानी से बिजली कैसे उत्पन्न होती है?)
बांधों में बहुत सारा पानी इकट्ठा करके उसे ऊंचाई से मशीनों (टर्बाइन) पर ज़ोर से गिराया जाता है। इससे मशीनें घूमती हैं और उसी से हमारी बिजली बनती है। इसलिए सही जवाब है: Water from lakes and rivers is stored in dams. This stored water is made to fall from a height onto the blades of turbines. The force turns the turbines, which generates energy. This energy is then converted into electricity.

Sawaal 4.33. How many days does it take the earth to revolve around the sun? (पृथ्वी को सूर्य का चक्कर लगाने में कितने दिन लगते हैं?)
बच्चों, हमारी पृथ्वी को सूरज का एक पूरा गोल चक्कर लगाने में 365 ¼ दिन (यानी पूरा एक साल) लगते हैं। इसलिए सही जवाब है: The earth takes 365 ¼ days (one year) to complete one revolution around the sun.

Sawaal 4.34. How many types of movements of the earth are there? (पृथ्वी की गतियां कितने प्रकार की होती हैं?)
हमारी पृथ्वी दो तरह से घूमती है: पहला, अपनी ही जगह पर लट्टू की तरह (Rotation), और दूसरा, सूरज के चारों तरफ (Revolution)। इसलिए सही जवाब है: There are two main types of movements of the earth: Rotation and Revolution.

Sawaal 4.35. What causes days and nights? (दिन और रात किसके कारण होते हैं?)
जब पृथ्वी लट्टू की तरह अपनी जगह पर घूमती है, तो जो हिस्सा सूरज के सामने आता है वहां दिन होता है और पीछे वाले हिस्से में रात हो जाती है। इसलिए सही जवाब है: The rotation of the earth on its own axis causes day and night.
"""

lines_in_data = evs_data.split('\n')
slides = []

current_question = ""
current_answer = []
is_heading = False

for line in lines_in_data:
    line = line.strip()
    if not line: continue
        
    if line.startswith("Sawaal") or line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4."):
        if current_question:
            slides.append({
                "question": current_question,
                "answer": '\n'.join(current_answer),
                "is_heading": is_heading
            })
            
        current_question = line
        current_answer = []
        is_heading = not line.startswith("Sawaal")
    else:
        current_answer.append(line)

if current_question:
    slides.append({
        "question": current_question,
        "answer": '\n'.join(current_answer),
        "is_heading": is_heading
    })

@app.route('/')
def index():
    return render_template('index.html', total_slides=len(slides))

@app.route('/get_slide/<int:slide_id>')
def get_slide(slide_id):
    if 0 < slide_id <= len(slides):
        data = slides[slide_id - 1].copy()
        data['audio'] = f"/static/audios/slide_{slide_id}.mp3"
        return jsonify(data)
    return jsonify({"error": "Slide not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
