#include <vector>
#include <opencv2/opencv.hpp>

int main(int argc, char* argv[]){
    // create VideoCapture object
    cv::VideoCapture cap(0);
    // Declare "image" as cv::Mat type variable
    cv::Mat image;
    
    int delay = 33;
    // Open first detected webcam
    //cap.open(0);
    // Capture webcam frames only when it is only opened
    while(cap.isOpened()){
        cap>>image;
        // Create a mirror effect of the frame
        cv::flip(image,image,1);
        // Display frames in a window
        cv::imshow("My Webcam Stream",image);

        //Create a waitKey for delay and detect keypress to exit the app
        int key = cv::waitKey(delay) & 255;
        if (key == 'p') {
            delay = (delay == 0) ? 33 : 0;
        } else if (key == 27) {
            break;
        }
    }
    return EXIT_SUCCESS;
}
