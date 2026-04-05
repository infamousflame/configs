.PHONY: test

test:
	@Xephyr -br -ac :90 -screen 1280x720 & \
	sleep 1 && \
	DISPLAY=:90 qtile start -c config.py
