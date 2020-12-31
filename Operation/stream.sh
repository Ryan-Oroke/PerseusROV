cp ./rovstream.html ../../mjpg-streamer/mjpg-streamer-experimental/

cd ../..
cd mjpg-streamer/
cd mjpg-streamer-experimental/

./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
