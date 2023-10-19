#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#
# Izzy Ganteng

FROM ayiinxd/ayiin:xd

RUN git clone -b Ebow-Userbot https://github.com/c0dsx/Ebow-Userbot /home/ebowuserbot/ \
    && chmod 777 /home/ebowuserbot \
    && mkdir /home/ebowuserbot/bin/

#COPY ./sample.env ./.env* /home/ebowuserbot/

WORKDIR /home/ebowuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
