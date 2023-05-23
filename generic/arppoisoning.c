#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <signal.h>
#include <unistd.h>
#include <pcap.h>
#include <libnet.h>

int main(int argc, char **argv)
{
char *dev = NULL;
char errbuf[PCAP_ERRBUF_SIZE];
pcap_t *handle;
struct pcap_pkthdr header;
const u_char *packet;
libnet_t *lnet;
char *device = "eth0";
int count = 0;
u_int32_t ipaddr;
u_char macaddr[6];

//Initialize libnet
lnet = libnet_init(LIBNET_RAW4, device, errbuf);
if (lnet == NULL)
{
    fprintf(stderr, "libnet_init() failed: %s\n", errbuf);
    exit(EXIT_FAILURE);
}

//Get IP and MAC addresses of target
ipaddr = libnet_name2addr4(lnet, argv[1], LIBNET_RESOLVE);
libnet_autobuild_ethernet(lnet, NULL, macaddr);
libnet_autobuild_ipv4(lnet, 0, IPPROTO_UDP, ipaddr, 0, 0);
libnet_autobuild_udp(lnet, 5000, 5000, 8, 0, NULL, 0);

//Send packet
if (libnet_write(lnet) == -1)
{
    fprintf(stderr, "libnet_write() failed: %s\n", libnet_geterror(lnet));
    exit(EXIT_FAILURE);
}

//Cleanup
libnet_destroy(lnet);
return 0;

}
