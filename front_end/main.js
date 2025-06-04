const productListDiv = document.getElementById('product-list');

const apiUrl = 'http://127.0.0.1:8000/api/products/';

async function fetchandDisplay(){
    /**
     * An asynchronous function to fetch and Display Products
     */
    try{
        productListDiv.innerHTML = '<p>Loading products</p>';

        response = await fetch(apiUrl);
        if (!response.ok){
            throw new Error(`Http Error! Status: ${response.status}- ${response.statusText}`);
        }
        const products = await response.json();
        productListDiv.innerHTML = '';
        
        if (products.length === 0) {
            productListDiv.innerHTML = '<p>No products found yet. Add some</p>'
            return;
        }
        products.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';

            productCard.innerHTML = `
                <h3>${product.name}</h3>
                <p>Price${product.price}</p>
                <p>Description: ${product.description || 'No description'}</p>
                <p>Brand: ${product.brand_name || 'N/A'}</p>
                <p>Category: ${product.category_name || 'N/A'}</p>
                <img src="${product.image_url || 'https://via.placeholder.com/150'}" alt="${product.name}" style="max-width:150px;">
            `;
            productListDiv.appendChild(productCard);
        });
    } catch (error) {
        console.error('Error fetching or displaying products:', error);
        productListDiv.innerHTML = `<p style="color: red;">Failed to  load products. Please check console for details. error: ${error.message}</p>`;
    }
}
fetchandDisplay();