using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

public class UDPListener : MonoBehaviour
{
    Thread receiveThread;
    UdpClient client;
    public int port = 5065; 

    void Start()
    {
        InitializeUDPListener();
    }

    private void InitializeUDPListener()
    {
        receiveThread = new Thread(new ThreadStart(ReceiveData));
        receiveThread.IsBackground = true;
        receiveThread.Start();
    }

    private void ReceiveData()
    {
        client = new UdpClient(port);
        while (true)
        {
            try
            {
                IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);
                byte[] data = client.Receive(ref anyIP);

                string text = Encoding.UTF8.GetString(data);
                Debug.Log(">> " + text);
                
              
            }
            catch (Exception err)
            {
                print(err.ToString());
            }
        }
    }

    void OnApplicationQuit()
    {
        if (receiveThread != null) receiveThread.Abort();
        client.Close();
    }
}
