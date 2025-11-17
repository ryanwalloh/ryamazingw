## Reading-Time Estimates

We display a `MIN READ` chip on each blog card. This chip helps readers judge
how long an article may take, combining the words in the main body and the
estimated time spent on inline media.

### 1. Word Count Source
- We copy the HTML for each article into `pages/articles/<article>.html`.
- The body of the article must be wrapped in `.blog-post-container`. When we
  compute word counts in development (via quick scripts) or future automation,
  we extract the text inside this container.
- Only visible text counts. Hidden markup, attributes, scripts, etc. do not.

### 2. Word Count Tracking
- For now, we manually set a `data-word-count` attribute on the `blog-chip--time`
  element in `pages/blog.html`. Example:

  ```html
  <span class="blog-chip blog-chip--time"
        data-word-count="1071"
        data-article-path="articles/article1.html">
  </span>
  ```

### 3. Reading Speed Assumptions
- Fast reading pace: 250 wpm
- Slow reading pace: 200 wpm

We round up the minutes, then add the media buffer (see below).

### 4. Image/Media Buffer
- Each chip optionally includes `data-article-path`. The client fetches that
  HTML, counts `<img>` elements within `.blog-post-container`, and adds a buffer.
- Buffer = `ceil(image_count * 8 seconds / 60)`, minimum 1 minute. Images
  without `data-article-path` fall back to 1 minute.
- Buffers are cached during the session.

### 5. Display Rules
- If slow & fast estimates (after adding buffer) match, we show `X MIN READ`.
- Otherwise, we show `X-Y MIN READ`.

### 6. Adding New Articles
1. Create `pages/articles/<article>.html`.
2. Wrap the article content in `.blog-post-container`.
3. Update the relevant card in `pages/blog.html`:
   - Set `data-word-count` to the body word count (use the same script/process).
   - Add `data-article-path="articles/<article>.html"`.

### 7. Future Enhancements
- Automate word counts + metadata (ex: on build) and populate the chip via
  JSON/frontmatter.
- Extend buffer logic to include videos or long captions.

