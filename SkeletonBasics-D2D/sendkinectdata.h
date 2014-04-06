#ifndef SENDKINECTDATA_H
#define SENDKINECTDATA_H

#define SERVER "192.168.1.5"
#define PORT "5050"

class SendKinectData{
	int sfd;
public:
	SendKinectData();
	~SendKinectData();
	int sendData(D2D1_POINT_2F, D2D1_POINT_2F, D2D1_POINT_2F, D2D1_POINT_2F);
};

#endif