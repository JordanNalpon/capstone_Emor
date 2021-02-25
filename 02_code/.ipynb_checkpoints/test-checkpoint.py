{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "athletic-clinic",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape (<ipython-input-1-52f8eea4c9c5>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-1-52f8eea4c9c5>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    videoWriter = cv2.VideoWriter('C:\\Users\\JDN\\Desktop\\Github\\ga_capstone\\01_materials\\exported_materials\\testvideo.avi', fourcc, 30.0, (640,480))\u001b[0m\n\u001b[1;37m                                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import sys\n",
    "sys.stdout.write(\"Hello\")\n",
    " \n",
    "capture = cv2.VideoCapture(0)\n",
    " \n",
    "fourcc = cv2.VideoWriter_fourcc('X','V','I','D')\n",
    "videoWriter = cv2.VideoWriter('C:\\Users\\JDN\\Desktop\\Github\\ga_capstone\\01_materials\\exported_materials\\testvideo.avi', fourcc, 30.0, (640,480))\n",
    "print('print works')\n",
    "if not (capture.isOpened()):\n",
    "    print(\"Cannot open camera\")\n",
    "    exit()\n",
    "print(capture)\n",
    "\n",
    "while (capture.isOpened()):\n",
    " \n",
    "    ret, frame = capture.read()\n",
    "     \n",
    "    if ret:\n",
    "        cv2.imshow('video', frame)\n",
    "        videoWriter.write(frame)\n",
    " \n",
    "    if cv2.waitKey(1) == 27:\n",
    "        break\n",
    " \n",
    "capture.release()\n",
    "videoWriter.release()\n",
    " \n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
