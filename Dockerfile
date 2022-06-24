FROM python

WORKDIR /bot

COPY . /bot

#RUN apt-get install tzdata
#ENV TZ=Asia/Yekaterinburg
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install aiogram
RUN pip install asyncio
#RUN pip install aioschedule
RUN pip install datetime
RUN pip install --upgrade pip
RUN pip install --upgrade google-api-python-client
RUN pip install --upgrade oauth2client 
RUN pip install bs4

CMD [ "python3", "bot_start.py" ]