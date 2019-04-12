# Diffie Hellman Key Exchange 

From [Wiki](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)

The simplestimplementation of the protocol uses the multiplicative group of integers modulo p, where p is prime, and g is a primitive root modulo p. These two values are chosen in this way to ensure that the resulting shared secret can take on any value from 1 to p–1.

1. A and B shares $p$ and $g$, where $g$ is a primitive root of $p$;
2. A chooses secret $s$ and send to Bob $S = g^s % p$
3. B chooses secret $h$ and send to Bob $H = g^h % p$
4. A compute $k = H^s$
5. B compute $k = S^h$

$k$ is the shared key between A and B.