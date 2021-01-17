import face
import camera
import mask


def main():
    print("Face Mask Detection System V1.0/nThank you for using")

    while True:
        camera.takePicture(10)

        if face.detectFace("/home/pi/Desktop/mask-detector/p.jpg") > 0:
            # face detected, check if mask

            if mask.detectMask("/home/pi/Desktop/mask-detector/p.jpg"):
                print("Mask Detected, thank you")
            else:
                print("Mask not found, please put a mask on before entering")

        camera.deletePicture()


if __name__ == "__main__":
    main()