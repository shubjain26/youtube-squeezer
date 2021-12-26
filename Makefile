buildd:
	docker build -t youtube-squeezer .


rund:
	docker run -it -v `pwd`/downloads:/app/downloads youtube-squeezer