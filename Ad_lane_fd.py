{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "error",
     "evalue": "/tmp/build/80754af9/opencv_1512491964794/work/modules/imgproc/src/drawing.cpp:2398: error: (-215) p.checkVector(2, 4) >= 0 in function fillPoly\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31merror\u001b[0m                                     Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-7-72ed206c2d1d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    372\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    373\u001b[0m \u001b[0mimage\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmpimg\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mimread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'test_images/straight_lines2.jpg'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 374\u001b[0;31m \u001b[0mtest_image\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mad_lane_finding_pipeline\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    375\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mimshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtest_image\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    376\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-7-72ed206c2d1d>\u001b[0m in \u001b[0;36mad_lane_finding_pipeline\u001b[0;34m(img)\u001b[0m\n\u001b[1;32m    366\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    367\u001b[0m     \u001b[0;31m#final_image = draw_poly_lines(poly_image, left_fitx, right_fitx, ploty)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 368\u001b[0;31m     \u001b[0mnext_step\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdraw_poly_lines\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpoly_image\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mleft_fitx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mright_fitx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mploty\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    369\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mpoly_image\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    370\u001b[0m \u001b[0;31m# Run the functions\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-7-72ed206c2d1d>\u001b[0m in \u001b[0;36mdraw_poly_lines\u001b[0;34m(binary_warped, left_fitx, right_fitx, ploty)\u001b[0m\n\u001b[1;32m    344\u001b[0m     \u001b[0mlane_pts\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhstack\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mleft_lane_pts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mright_lane_pts\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    345\u001b[0m     \u001b[0;31m# Draw the lane onto the warped blank image\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 346\u001b[0;31m     \u001b[0mcv2\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfillPoly\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mout_img\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlane_pts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m255\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    347\u001b[0m     \u001b[0;31m# Warp the blank back to original image space using inverse perspective matrix (Minv)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    348\u001b[0m     \u001b[0munwarp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0munwarp\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mout_img\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31merror\u001b[0m: /tmp/build/80754af9/opencv_1512491964794/work/modules/imgproc/src/drawing.cpp:2398: error: (-215) p.checkVector(2, 4) >= 0 in function fillPoly\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fc0abfd69b0>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "### import pickle\n",
    "import cv2\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.image as mpimg\n",
    "import glob\n",
    "from moviepy.editor import VideoFileClip\n",
    "\n",
    "################Distortion correction calculated via camera calibration###########\n",
    "\n",
    "# Adjustable checkerboard Dimensions\n",
    "cbrow = 6\n",
    "cbcol = 9\n",
    "\n",
    "# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)\n",
    "objp = np.zeros((cbrow * cbcol, 3), np.float32)\n",
    "objp[:, :2] = np.mgrid[0:cbcol, 0:cbrow].T.reshape(-1, 2)\n",
    "\n",
    "# Arrays to store object points and image points from all the images.\n",
    "objpoints = [] # 3d points in real world space\n",
    "imgpoints = [] # 2d points in image plane.\n",
    "\n",
    "# Make a list of calibration images\n",
    "images = glob.glob('camera_cal/calibration*.jpg')\n",
    "\n",
    "# Step through the list and search for chessboard corners\n",
    "for idx, fname in enumerate(images):\n",
    "    cal_img = cv2.imread(fname)\n",
    "    gray = cv2.cvtColor(cal_img, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "# Find Chessboard corners\n",
    "    ret, corners = cv2.findChessboardCorners(gray, (9,6), None)\n",
    "\n",
    "    if ret == True:\n",
    "        objpoints.append(objp)\n",
    "        imgpoints.append(corners)\n",
    "\n",
    "def cal_undistort(img, objpoints, imgpoints):\n",
    "    # Use cv2.calibrateCamera() and cv2.undistort()\n",
    "    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape[::-1], None, None)\n",
    "    undist = cv2.undistort(img, mtx, dist, None, mtx)\n",
    "    return undist\n",
    "\n",
    "\n",
    "################Pipeline For Binary Image###########\n",
    "\n",
    "#images = glob.glob('test_images/*.jpg')\n",
    "\n",
    "def abs_sobel_thresh(img, orient='x', thresh_min=30, thresh_max=255):\n",
    "    # Convert to grayscale\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)\n",
    "    # Apply x or y gradient with the OpenCV Sobel() function\n",
    "    # and take the absolute value\n",
    "    if orient == 'x':\n",
    "        abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0))\n",
    "    if orient == 'y':\n",
    "        abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 0, 1))\n",
    "    # Rescale back to 8 bit integer\n",
    "    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))\n",
    "    # Create a copy and apply the threshold\n",
    "    binary_output = np.zeros_like(scaled_sobel)\n",
    "    # Here I'm using inclusive (>=, <=) thresholds, but exclusive is ok too\n",
    "    binary_output[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1\n",
    "\n",
    "    # Return the result\n",
    "    return binary_output\n",
    "\n",
    "def dir_threshold(img, sobel_kernel=3, thresh=(0, np.pi/2)):\n",
    "    \n",
    "    # Apply the following steps to img\n",
    "    # 1) Convert to grayscale\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)\n",
    "    # 2) Take the gradient in x and y separately\n",
    "    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)\n",
    "    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)\n",
    "    # 3) Take the absolute value of the x and y gradients\n",
    "    gradmag = np.sqrt(sobelx**2 + sobely**2)\n",
    "    # 4) Use np.arctan2(abs_sobely, abs_sobelx) to calculate the direction of the gradient \n",
    "    absgraddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))\n",
    "    # 5) Create a binary mask where direction thresholds are met\n",
    "    # 6) Return this mask as your binary_output image\n",
    "    binary_output =  np.zeros_like(absgraddir)\n",
    "    binary_output[(absgraddir >= thresh[0]) & (absgraddir <= thresh[1])] = 1\n",
    "    #binary_output = np.copy(img) # Remove this line\n",
    "    return binary_output\n",
    "\n",
    "\n",
    "# Define a function to return the magnitude of the gradient\n",
    "# for a given sobel kernel size and threshold values\n",
    "def mag_thresh(img, sobel_kernel=3, mag_thresh=(0, 255)):\n",
    "    # Convert to grayscale\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "    # Take both Sobel x and y gradients\n",
    "    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)\n",
    "    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)\n",
    "    # Calculate the gradient magnitude\n",
    "    gradmag = np.sqrt(sobelx**2 + sobely**2)\n",
    "    # Rescale to 8 bit\n",
    "    scale_factor = np.max(gradmag)/255 \n",
    "    gradmag = (gradmag/scale_factor).astype(np.uint8) \n",
    "    # Create a binary image of ones where threshold is met, zeros otherwise\n",
    "    binary_output = np.zeros_like(gradmag)\n",
    "    binary_output[(gradmag >= mag_thresh[0]) & (gradmag <= mag_thresh[1])] = 1\n",
    "\n",
    "    # Return the binary image\n",
    "    return binary_output\n",
    "\n",
    "def clr_thresh(img, s_thresh=(170, 255), sx_thresh=(20, 100)):\n",
    "    img = np.copy(img)\n",
    "    # Convert to HLS color space and separate the V channel\n",
    "    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)\n",
    "    l_channel = hls[:,:,1]\n",
    "    s_channel = hls[:,:,2]\n",
    "    # Sobel x\n",
    "    sobelx = cv2.Sobel(l_channel, cv2.CV_64F, 1, 0) # Take the derivative in x\n",
    "    abs_sobelx = np.absolute(sobelx) # Absolute x derivative to accentuate lines away from horizontal\n",
    "    scaled_sobel = np.uint8(255*abs_sobelx/np.max(abs_sobelx))\n",
    "    \n",
    "    # Threshold x gradient\n",
    "    sxbinary = np.zeros_like(scaled_sobel)\n",
    "    sxbinary[(scaled_sobel >= sx_thresh[0]) & (scaled_sobel <= sx_thresh[1])] = 1\n",
    "    \n",
    "    # Threshold color channel\n",
    "    s_binary = np.zeros_like(s_channel)\n",
    "    s_binary[(s_channel >= s_thresh[0]) & (s_channel <= s_thresh[1])] = 1\n",
    "    # Stack each channel\n",
    "    color_binary = np.dstack(( np.zeros_like(sxbinary), sxbinary, s_binary)) * 255\n",
    "    return color_binary\n",
    "\n",
    "\n",
    "def find_lane_pixels(binary_warped):\n",
    "    # Take a histogram of the bottom half of the image\n",
    "    histogram = np.sum(binary_warped[binary_warped.shape[0]//2:,:], axis=0)\n",
    "    # Create an output image to draw on and visualize the result\n",
    "    out_img = np.dstack((binary_warped, binary_warped, binary_warped))\n",
    "    # Find the peak of the left and right halves of the histogram\n",
    "    # These will be the starting point for the left and right lines\n",
    "    midpoint = np.int(histogram.shape[0]//2)\n",
    "    leftx_base = np.argmax(histogram[:midpoint])\n",
    "    rightx_base = np.argmax(histogram[midpoint:]) + midpoint\n",
    "\n",
    "    # HYPERPARAMETERS\n",
    "    # Choose the number of sliding windows\n",
    "    nwindows = 9\n",
    "    # Set the width of the windows +/- margin\n",
    "    margin = 100\n",
    "    # Set minimum number of pixels found to recenter window\n",
    "    minpix = 50\n",
    "\n",
    "    # Set height of windows - based on nwindows above and image shape\n",
    "    window_height = np.int(binary_warped.shape[0]//nwindows)\n",
    "    # Identify the x and y positions of all nonzero pixels in the image\n",
    "    nonzero = binary_warped.nonzero()\n",
    "    nonzeroy = np.array(nonzero[0])\n",
    "    nonzerox = np.array(nonzero[1])\n",
    "    # Current positions to be updated later for each window in nwindows\n",
    "    leftx_current = leftx_base\n",
    "    rightx_current = rightx_base\n",
    "\n",
    "    # Create empty lists to receive left and right lane pixel indices\n",
    "    left_lane_inds = []\n",
    "    right_lane_inds = []\n",
    "\n",
    "    # Step through the windows one by one\n",
    "    for window in range(nwindows):\n",
    "        # Identify window boundaries in x and y (and right and left)\n",
    "        win_y_low = binary_warped.shape[0] - (window+1)*window_height\n",
    "        win_y_high = binary_warped.shape[0] - window*window_height\n",
    "        win_xleft_low = leftx_current - margin\n",
    "        win_xleft_high = leftx_current + margin\n",
    "        win_xright_low = rightx_current - margin\n",
    "        win_xright_high = rightx_current + margin\n",
    "        \n",
    "        # Draw the windows on the visualization image\n",
    "        cv2.rectangle(out_img,(win_xleft_low,win_y_low),\n",
    "        (win_xleft_high,win_y_high),(0,255,0), 2) \n",
    "        cv2.rectangle(out_img,(win_xright_low,win_y_low),\n",
    "        (win_xright_high,win_y_high),(0,255,0), 2) \n",
    "        \n",
    "        # Identify the nonzero pixels in x and y within the window #\n",
    "        good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & \n",
    "        (nonzerox >= win_xleft_low) &  (nonzerox < win_xleft_high)).nonzero()[0]\n",
    "        good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & \n",
    "        (nonzerox >= win_xright_low) &  (nonzerox < win_xright_high)).nonzero()[0]\n",
    "        \n",
    "        # Append these indices to the lists\n",
    "        left_lane_inds.append(good_left_inds)\n",
    "        right_lane_inds.append(good_right_inds)\n",
    "     \n",
    "        \n",
    "        # If you found > minpix pixels, recenter next window on their mean position\n",
    "        if len(good_left_inds) > minpix:\n",
    "            leftx_current = np.int(np.mean(nonzerox[good_left_inds]))\n",
    "        if len(good_right_inds) > minpix:        \n",
    "            rightx_current = np.int(np.mean(nonzerox[good_right_inds]))\n",
    "\n",
    "    # Concatenate the arrays of indices (previously was a list of lists of pixels)\n",
    "    try:\n",
    "        left_lane_inds = np.concatenate(left_lane_inds)\n",
    "        right_lane_inds = np.concatenate(right_lane_inds)\n",
    "       \n",
    "    except ValueError:\n",
    "        # Avoids an error if the above is not implemented fully\n",
    "        pass\n",
    "\n",
    "    # Extract left and right line pixel positions\n",
    "    leftx = nonzerox[left_lane_inds]\n",
    "    lefty = nonzeroy[left_lane_inds] \n",
    "    rightx = nonzerox[right_lane_inds]\n",
    "    righty = nonzeroy[right_lane_inds]\n",
    "    \n",
    "\n",
    "    return leftx, lefty, rightx, righty, out_img\n",
    "\n",
    "\n",
    "def fit_polynomial(binary_warped):\n",
    "    # Find our lane pixels first\n",
    "    leftx, lefty, rightx, righty, out_img = find_lane_pixels(binary_warped)\n",
    "\n",
    "    # Fit a second order polynomial to each using `np.polyfit`\n",
    "    left_fit = np.polyfit(lefty, leftx, 2)\n",
    "    right_fit = np.polyfit(righty, rightx, 2)\n",
    "\n",
    "\n",
    "    # Generate x and y values for plotting\n",
    "    ploty = np.linspace(0, binary_warped.shape[0]-1, binary_warped.shape[0] )\n",
    "    try:\n",
    "        left_fitx = left_fit[0]*ploty**2 + left_fit[1]*ploty + left_fit[2]\n",
    "        right_fitx = right_fit[0]*ploty**2 + right_fit[1]*ploty + right_fit[2]\n",
    "    except TypeError:\n",
    "        # Avoids an error if `left` and `right_fit` are still none or incorrect\n",
    "        print('The function failed to fit a line!')\n",
    "        left_fitx = 1*ploty**2 + 1*ploty\n",
    "        right_fitx = 1*ploty**2 + 1*ploty\n",
    "\n",
    "    ## Visualization ##\n",
    "    # Colors in the left and right lane regions\n",
    "    out_img[lefty, leftx] = [255, 0, 0]\n",
    "    out_img[righty, rightx] = [0, 0, 255]\n",
    "\n",
    "    # Plots the left and right polynomials on the lane lines\n",
    "    plt.plot(left_fitx, ploty, color='yellow')\n",
    "    plt.plot(right_fitx, ploty, color='yellow')\n",
    "    #cv2.imwrite('fp.jpg', plt.plot(left_fitx, ploty, color='yellow'))\n",
    "    return out_img, left_fitx, right_fitx, ploty\n",
    "\n",
    "def warp(img):\n",
    "\n",
    "    img_size = (img.shape[1], img.shape[0])\n",
    "    #Four source coordinates\n",
    "    src = np.float32(\n",
    "        [[585,460],\n",
    "         [1127,720],\n",
    "         [200,720],\n",
    "         [695,460]])\n",
    "    \n",
    "    #Four desired coordinates\n",
    "    dst = np.float32(\n",
    "        [[320,0],\n",
    "         [960,720],\n",
    "         [320,720],\n",
    "         [960,0]])\n",
    "    \n",
    "    #Compute perspective transform, M\n",
    "    M = cv2.getPerspectiveTransform(src, dst)\n",
    "    \n",
    "    #Compute inverse perspective transform, Minv\n",
    "    Minv = cv2.getPerspectiveTransform(dst, src)\n",
    "    \n",
    "    #Create warped image using linar interpolation\n",
    "    warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_NEAREST)\n",
    "    return warped\n",
    "\n",
    "\n",
    "def unwarp(img):\n",
    "\n",
    "    img_size = (img.shape[1], img.shape[0])\n",
    "    #Four source coordinates\n",
    "    src = np.float32(\n",
    "        [[585,460],\n",
    "         [1127,720],\n",
    "         [200,720],\n",
    "         [695,460]])\n",
    "    \n",
    "    #Four desired coordinates\n",
    "    dst = np.float32(\n",
    "        [[320,0],\n",
    "         [960,720],\n",
    "         [320,720],\n",
    "         [960,0]])\n",
    "    \n",
    "    #Compute perspective transform, M\n",
    "    M = cv2.getPerspectiveTransform(src, dst)\n",
    "    \n",
    "    #Compute inverse perspective transform, Minv\n",
    "    Minv = cv2.getPerspectiveTransform(dst, src)\n",
    "    \n",
    "    #Create warped image using linar interpolation\n",
    "    unwarped = cv2.warpPerspective(img, Minv, img_size, flags=cv2.INTER_NEAREST)\n",
    "    return unwarped\n",
    "\n",
    "def measure_curvature_pixels():\n",
    "    '''\n",
    "    Calculates the curvature of polynomial functions in pixels.\n",
    "    '''\n",
    "    # Start by generating our fake example data\n",
    "    # Make sure to feed in your real data instead in your project!\n",
    "    ploty, left_fit, right_fit = generate_data()\n",
    "    \n",
    "    # Define y-value where we want radius of curvature\n",
    "    # We'll choose the maximum y-value, corresponding to the bottom of the image\n",
    "    y_eval = np.max(ploty)\n",
    "    \n",
    "    # Calculation of R_curve (radius of curvature)\n",
    "    left_curverad = ((1 + (2*left_fit[0]*y_eval + left_fit[1])**2)**1.5) / np.absolute(2*left_fit[0])\n",
    "    right_curverad = ((1 + (2*right_fit[0]*y_eval + right_fit[1])**2)**1.5) / np.absolute(2*right_fit[0])\n",
    "    \n",
    "    return left_curverad, right_curverad\n",
    "\n",
    "def fit_poly(img_shape, leftx, lefty, rightx, righty):\n",
    "     ### TO-DO: Fit a second order polynomial to each with np.polyfit() ###\n",
    "    left_fit = np.polyfit(lefty, leftx, 2)\n",
    "    right_fit = np.polyfit(righty, rightx, 2)\n",
    "    print(left_fit)\n",
    "    # Generate x and y values for plotting\n",
    "    ploty = np.linspace(0, img_shape[0]-1, img_shape[0])\n",
    "    ### TO-DO: Calc both polynomials using ploty, left_fit and right_fit ###\n",
    "    left_fitx = left_fit[0]*ploty**2 + left_fit[1]*ploty + left_fit[2]\n",
    "    right_fitx = right_fit[0]*ploty**2 + right_fit[1]*ploty + right_fit[2]\n",
    "    return left_fitx, right_fitx, ploty\n",
    "\n",
    "\n",
    "\n",
    "def draw_poly_lines(binary_warped, left_fitx, right_fitx, ploty):     \n",
    "    # Create an image to draw on and an image to show the selection window\n",
    "    out_img = np.dstack((binary_warped, binary_warped, binary_warped))*255\n",
    "    window_img = np.zeros_like(out_img)\n",
    "\n",
    "    \n",
    "\n",
    "    # Recast the x and y points into usable format for cv2.fillPoly()\n",
    "    left_lane_pts = np.array([np.transpose(np.vstack([left_fitx, ploty]))])\n",
    "    right_lane_pts = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])\n",
    "    lane_pts = np.hstack((left_lane_pts, right_lane_pts))\n",
    "    # Draw the lane onto the warped blank image\n",
    "    cv2.fillPoly(out_img, lane_pts, (0,255, 0))\n",
    "    # Warp the blank back to original image space using inverse perspective matrix (Minv)\n",
    "    unwarp = unwarp(out_img) \n",
    "    # Combine the result with the original image\n",
    "    result = cv2.addWeighted(binary_warped, 1, unwarp, 0.3, 0)\n",
    "    \n",
    "    return result\n",
    "\n",
    "def ad_lane_finding_pipeline(img):\n",
    "    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "    pers_transform = warp(img)\n",
    "    hls_img = clr_thresh(pers_transform, s_thresh=(170, 255), sx_thresh=(20, 100))\n",
    "    gradx = abs_sobel_thresh(pers_transform, orient='x', thresh_min=20, thresh_max=100)\n",
    "    grady = abs_sobel_thresh(pers_transform, orient='y', thresh_min=20, thresh_max=100)\n",
    "    mag_binary = mag_thresh(pers_transform, sobel_kernel=3, mag_thresh=(50, 255))\n",
    "    dir_binary = dir_threshold(pers_transform, sobel_kernel=3, thresh=(0, np.pi/2))\n",
    "    combined = np.zeros_like(dir_binary)\n",
    "    combined[((gradx == 1) & (grady == 1)) | ((mag_binary == 1) & (dir_binary == 1))] = 1\n",
    "    poly_image, left_fitx, right_fitx, ploty = fit_polynomial(combined)\n",
    "\n",
    "    \n",
    "    #final_image = draw_poly_lines(poly_image, left_fitx, right_fitx, ploty)\n",
    "    next_step = draw_poly_lines(poly_image, left_fitx, right_fitx, ploty)\n",
    "    return poly_image\n",
    "# Run the functions\n",
    "\n",
    "\n",
    "image = mpimg.imread('test_images/straight_lines2.jpg')\n",
    "test_image = ad_lane_finding_pipeline(image)\n",
    "plt.imshow(test_image)\n",
    "plt.show()\n",
    "\n",
    "\n",
    "#video_output = 'project_video_output.mp4'\n",
    "#clip1 = VideoFileClip(\"project_video.mp4\")\n",
    "#combined_clip = clip1.fl_image(ad_lane_finding_pipeline)\n",
    "#combined_clip.write_videofile(video_output, audio=False)\n",
    "\n",
    "\n",
    "#grad_binary = abs_sobel_thresh(undistorted, orient='x', thresh_min=20, thresh_max=100)\n",
    "# Plot the result\n",
    "#f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))\n",
    "#f.tight_layout()\n",
    "#ax1.imshow(img)\n",
    "#ax1.set_title('Original Image', fontsize=50)\n",
    "#ax2.imshow(img, cmap='gray')\n",
    "#ax2.set_title('Thresholded Gradient', fontsize=50)\n",
    "#plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
