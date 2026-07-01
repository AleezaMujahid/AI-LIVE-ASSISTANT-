# Deployment Guide for AI Live Assistant

This guide walks you through deploying the AI Live Assistant to production on Vercel.

## Prerequisites

- GitHub account with the project repository
- Vercel account (free tier available at vercel.com)
- OpenAI API key (get one at platform.openai.com/api-keys)

## Step-by-Step Deployment

### 1. Push Code to GitHub

First, ensure your code is pushed to GitHub:

```bash
git add .
git commit -m "deployment: prepare for production"
git push origin main
```

### 2. Create Vercel Project

#### Option A: Using Vercel Dashboard
1. Go to [vercel.com](https://vercel.com)
2. Click "Add New..." → "Project"
3. Import your GitHub repository
4. Select the repository and click "Import"

#### Option B: Using Vercel CLI
```bash
npm install -g vercel
vercel
```

### 3. Configure Environment Variables

In Vercel project settings:

1. Go to Settings → Environment Variables
2. Add the following variables:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key
   - **Environments**: Production, Preview, Development

```bash
# Or via CLI
vercel env add OPENAI_API_KEY
```

### 4. Deploy

#### Automatic Deployment
Every push to your main branch automatically triggers a deployment.

#### Manual Deployment
```bash
vercel --prod
```

### 5. Verify Deployment

1. Visit your Vercel project URL (e.g., `your-project.vercel.app`)
2. Test the chat functionality
3. Check Vercel dashboard for deployment logs

## Environment Variables Reference

### Required
- `OPENAI_API_KEY`: Your OpenAI API key

### Optional
- `AI_GATEWAY_API_KEY`: For Vercel AI Gateway integration

## Monitoring & Logs

### View Logs
1. Vercel Dashboard → Deployments → Select deployment
2. Click "Logs" to see build and runtime logs
3. Use `vercel logs` CLI command

### Monitor Performance
1. Vercel Dashboard → Analytics
2. Track page load times, Core Web Vitals
3. Monitor API usage

## Troubleshooting

### Build Fails with Module Not Found
```
Error: Cannot find module 'ai/react'
```

**Solution:**
1. Ensure `ai` and `@ai-sdk/openai` are in package.json dependencies
2. Run `npm install` locally first
3. Push updated `package-lock.json` to GitHub
4. Redeploy

### API Key Not Working
1. Verify key is set in Vercel Environment Variables
2. Check OpenAI API key validity at platform.openai.com
3. Ensure account has available API credits
4. Restart deployment after updating key

### Timeout Errors
The project has 60-second timeout configured for API routes. If requests timeout:
1. Check OpenAI API status
2. Monitor network latency
3. Consider upgrading response handling

### Cold Start Issues
First request after deployment may be slower:
- This is normal for serverless functions
- Subsequent requests are faster
- Use Vercel Pro for faster cold starts

## Scaling & Performance

### Current Configuration
- **Framework**: Next.js with automatic static optimization
- **API Timeout**: 60 seconds
- **Region**: iad1 (Iowa, USA) - modify in vercel.json

### Optimize Performance
1. Enable Image Optimization in Vercel dashboard
2. Use Edge Functions for reduced latency (Vercel Pro)
3. Monitor Analytics for bottlenecks

### Change Regions
Edit `vercel.json`:
```json
{
  "regions": ["iad1", "sfo1", "lhr1"]
}
```

## Rollback Deployment

### Via Dashboard
1. Deployments → Select previous version
2. Click "..." → "Promote to Production"

### Via CLI
```bash
vercel deployments ls
vercel promote <deployment-id>
```

## CI/CD Integration

The project automatically:
1. Runs on every push to main
2. Builds with `npm run build`
3. Deploys if build succeeds
4. Creates preview deployments for PRs

### Custom Build Settings (if needed)
Edit `vercel.json`:
```json
{
  "buildCommand": "npm run build",
  "env": {
    "CUSTOM_VAR": "@custom_var"
  }
}
```

## Security Best Practices

1. **Never expose API keys** in code or logs
2. **Use Vercel's secret management** for sensitive data
3. **Enable authentication** if needed (implement in middleware)
4. **Monitor API usage** for unusual patterns
5. **Rotate API keys** periodically
6. **Use environment-specific keys** when possible

## Cost Management

### Monitor Costs
1. Vercel Dashboard → Settings → Usage
2. Check bandwidth and build minutes
3. OpenAI Platform → Usage for API costs

### Reduce Costs
- Use caching where appropriate
- Monitor token usage
- Consider rate limiting
- Use streaming responses (already implemented)

## Custom Domain

1. Add domain in Vercel: Settings → Domains
2. Update DNS records pointing to Vercel
3. Enable SSL/TLS (automatic with Vercel)

## Maintenance

### Regular Tasks
- Monitor error logs in Vercel dashboard
- Review analytics weekly
- Check OpenAI API status for issues
- Update dependencies monthly

### Update Dependencies
```bash
npm update
git commit -m "chore: update dependencies"
git push
```

## Support & Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Next.js Documentation](https://nextjs.org/docs)
- [AI SDK Documentation](https://sdk.vercel.ai)
- [OpenAI Documentation](https://platform.openai.com/docs)

## Emergency Contacts

- Vercel Status: https://vercel-status.com
- OpenAI Status: https://status.openai.com
- Vercel Support: https://vercel.com/help

---

For detailed Next.js and development information, see [README.md](./README.md)
