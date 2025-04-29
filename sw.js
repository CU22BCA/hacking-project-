const FLAG_CACHE_NAME = 'flag-cache-v1';
const PLACEHOLDER_FLAG = 'CTF{s3rv1c3_w0rk3r_placeholder}'; // Replace with your actual flag
const FLAG_URL = '/flag';

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(FLAG_CACHE_NAME)
            .then(cache => {
                console.log('Service Worker installed and caching flag.');
                return cache.put(FLAG_URL, new Response(PLACEHOLDER_FLAG));
            })
    );
});

self.addEventListener('fetch', event => {
    if (event.request.url.endsWith(FLAG_URL)) {
        console.log('Fetching flag from cache.');
        event.respondWith(caches.match(FLAG_URL));
    }
});