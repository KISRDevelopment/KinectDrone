#ifndef HEADER1_H
#define HEADER1_H

#define SERVER "localhost"
#define PORT 5050

class SendKinectData{
	std::string server = SERVER;
	int port = PORT;
	int lelbow, relbow, lhand, rhand;
	int sfd;
	SendKinectData();
	~SendKinectData();
	int senddata(int, int, int, int);
};

#endif