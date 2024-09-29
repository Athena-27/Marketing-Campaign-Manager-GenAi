import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function GeneratedPostDetails() {
  const { id } = useParams();
  const [post, setPost] = useState(null);

  useEffect(() => {
    fetchGeneratedPost();
  }, []);

  const fetchGeneratedPost = async () => {
    try {
      const response = await fetch(`http://localhost:8000/campaign/${id}/generated_post`);
      if (!response.ok) {
        throw new Error(`Error fetching generated post: ${response.statusText}`);
      }
      const data = await response.json();
      setPost(data);
    } catch (err) {
      console.log(err);
    }
  };

  if (!post) return <p>Loading...</p>;

  return (
    <div className="generated-post-details">
      <h1>Generated Instagram Post</h1>
      <p><strong>Caption:</strong> {post.caption}</p>
      <p><strong>Hashtags:</strong> {post.hashtags}</p>
      <p><strong>Slogan:</strong> {post.slogan}</p>
      <p><strong>Image Description:</strong> {post.image_description}</p>
      <p><strong>Call to Action:</strong> {post.call_to_action}</p>
    </div>
  );
}

export default GeneratedPostDetails;
